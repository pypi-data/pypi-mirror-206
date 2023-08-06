import json
import os
import re
import shlex
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path as P
from shutil import which
from subprocess import PIPE, Popen, STDOUT, DEVNULL
from threading import Thread
from typing import Any, Callable, Dict, Iterable, List, Union

from ..utils import IterQueue
from ..cls import Delayed, Proxy, LazyLoad
from ..func import truncate_str
from ..log import forcelogger

forcelogger.addScheme("subprocess", "<[cyan]\[{extra[desc]}][/] [gray50]-[/] >{message}")


class SubprocessError(RuntimeError):
    pass


class Subprocess(Popen):
    """
    An enhanced version of Popen for calling subprocess, which can pass
    the output of stdout to variables in real time, and message the output of
    stderr through a logger according to certain rules.

    Args:
        cmd: Command or list of arguments.
        fail: Raises error for non-zero exit codes. Only raised when calling results or read. Defaults to True.
        desc: Brief description of the subprocess. Defaults to the program name of the subprocess.
        shell: Shell exec name, such as 'bash', 'zsh', etc.
        clean: Run in a clean environment. Only when shell is set.
        cwd: Current working dir for subprocess.
        level: minimum logging level for subprocess.
        filters: A list of regex patterns for messages to be filtered. Defaults to None.
        pattern: A dict of {output regex: func} mappings. Defaults see: `Subprocess.default_pattern`.
        stdout: Can be 'pipe', 'log' or 'result'. Defaults to 'result'.
        stderr: Can be 'pipe', 'log' or 'result'. Defaults to 'log'.
    """

    def __init__(
        self,
        cmd: Union[List[str], str],
        fail: Union[bool, str, Exception] = True,
        desc: str = None,
        shell: Union[str, bool] = None,
        clean=False,
        cwd: Union[P, str] = None,
        level: int = 20,
        filters: Iterable = None,
        pattern: Dict[str, Union[Callable, str]] = None,
        stdout: Union[str, int] = "result",
        stderr: Union[str, int] = "log",
        stdin: Union[str, int] = "pipe",
        **kw,
    ):
        self._desc = desc
        self.filters = filters
        self.pattern = pattern
        self.level = level
        self.fail = fail
        self.callbacks = [self._stop_read]
        self._daemons: List[Thread] = []
        self._results = IterQueue()

        # pipe spliting
        pipe_args = {"stdout": stdout, "stderr": stderr, "stdin": stdin}
        kws = {}
        for p, c in pipe_args.items():
            if isinstance(c, str):
                if c.lower() in ("pipe", "result", "log"):
                    kws[p] = PIPE
            else:
                kws[p] = c
        kws.update(kw)

        # shell cmd construct
        if shell:
            if isinstance(cmd, List):
                self.cmd = shlex.join([str(c) for c in cmd])
            else:
                self.cmd = cmd
            if not isinstance(shell, (str, P)):
                shell = "bash"
            if not which(shell):
                msg = f'"{shell}" is not found in your PATH, please note this feature is for linux only'
                raise FileNotFoundError(msg)
            if clean:
                prefix = f"env -i {shell} --norc --noprofile -c"
            else:
                prefix = f"{shell} --norc --noprofile -c"
            cmd = shlex.split(f"{prefix} {shlex.quote(self.cmd)}")
            super().__init__(cmd, cwd=cwd, **kws)
        else:
            # cmd parsing
            if isinstance(cmd, str):
                self.cmd = shlex.split(cmd)
            else:
                self.cmd = [str(c) for c in cmd]
            if cwd:
                self.cwd = P(cwd)
            else:
                self.cwd = cwd = P.cwd()
            super().__init__(self.cmd, cwd=cwd, **kws)

        # logger
        self.log = forcelogger.bind(scheme="subprocess", desc=Proxy(self.desc), minlevel=Proxy(self.level))

        # listen daemons
        if isinstance(stdout, str):
            if stdout.lower() == "result":
                self._start_daemon(self.stdout, self._as_result)
            elif stdout.lower() == "log":
                self._start_daemon(self.stdout, self._as_log)
        if isinstance(stderr, str):
            if stderr.lower() == "result":
                self._start_daemon(self.stderr, self._as_result)
            elif stderr.lower() == "log":
                self._start_daemon(self.stderr, self._as_log)
        self.log.debug(f'Started "{self._get_command(truncate=60)}".')

        # watchdog daemon
        self._start_watchdog()

    @property
    def desc(self):
        if self._desc:
            return self._desc
        elif isinstance(self.cmd, str):
            return f"shell {self.pid}"
        else:
            return self._desc or os.path.basename(self.cmd[0])

    @desc.setter
    def desc(self, value):
        self._desc = value

    def write(self, data: Union[bytes, str, List, Dict], close=False):
        if isinstance(data, (List, Dict)):
            data = json.dumps(data)
        if isinstance(data, str):
            data = data.encode()
        self.stdin.write(data)
        self.stdin.flush()
        if close:
            self.stdin.close()

    def read(self):
        """A generator that waits for next result as str."""
        for i in self._results.follow():
            if i is None:
                self.check(results=False)
                break
            yield i

    def results(self) -> Union[Dict, List[Any], List[str]]:
        """Wait for process to finish and return results as dict/list (if detected), or as list of str."""
        self.check()
        results = [i for i in self._results if i is not None]
        try:
            return json.loads("\n".join(results))
        except ValueError:
            return results

    @staticmethod
    def default_pattern(logger) -> Dict[str, Callable]:
        errors = {r".*%s.*" % k: logger.error for k in ["error", "fail"]}
        warnings = {r".*%s.*" % k: logger.warning for k in ["warning", "invalid"]}
        return {
            **errors,
            **warnings,
            r"^info:\s*(.*)": logger.info,
            r"^debug:\s*(.*)": logger.debug,
            r"^traceback.*": logger.debug,
            r".*": logger.info,
        }

    def wait(self, timeout=None):
        start = time.time()
        result = super().wait(timeout=timeout)
        for t in self._daemons:
            t.join(timeout=timeout + start - time.time() if timeout else None)
        return result

    def add_callback(self, callback: Delayed):
        self.callbacks.append(callback)

    def _stop_read(self):
        self._results.put(None)

    def check(self, fail=None, results=True, timeout=None):
        if self.wait(timeout=timeout):
            errlog = self.log.error if self.fail else self.log.warning
            command = self._get_command(truncate=20)
            errlog(f'Exit code {self.returncode} when running "{command}"')
            if results:
                r = [" " * 4 + i for i in self._results if i]
                if len(r):
                    msgs = ["Last outputs:", *r]
                    for m in msgs:
                        self.log.debug(m)
            if fail is None:
                fail = self.fail
            if fail:
                if isinstance(fail, Exception):
                    raise fail
                elif isinstance(fail, str):
                    raise SubprocessError(fail)
                else:
                    raise SubprocessError(command)

    def _start_watchdog(self):
        t = Thread(target=self._watchdog)
        t.daemon = True
        t.start()

    def _watchdog(self):
        super().wait()
        for c in self.callbacks:
            Delayed(c).trigger()

    def _start_daemon(self, stream, handler):
        t = Thread(
            target=self._proxy_lines,
            args=[stream, self._handler(handler)],
        )
        t.daemon = True
        t.start()
        self._daemons.append(t)

    def _as_result(self, line, **kw):
        self._results.put(line)

    def _as_log(self, line: str, last=None):
        if self.filters:
            if any(re.search(r, line) for r in self.filters):
                return None
        if isinstance(last, Callable) and re.match(r"\s", line):
            last(line)
            return last
        pattern = self.pattern or self.default_pattern(self.log)
        for p, func in pattern.items():
            if isinstance(func, str):
                func = getattr(self.log, func)
            regex = re.search(p, line, re.IGNORECASE)
            if not regex:
                continue
            groups = regex.groups()
            if not len(groups):
                func(regex.group(0))
                return func
            elif len(groups) == 1:
                func(groups[0])
                return func
            else:
                func(str(groups))
                return func

    def _get_command(self, truncate=0):
        """Get a truncated command."""
        if isinstance(self.cmd, str):
            command = self.cmd
        else:
            command = " ".join(shlex.quote(str(a)) for a in self.cmd)
        return truncate_str(command, truncate)

    @staticmethod
    def _handler(func):
        def handler(line, *args, **kw):
            return func(line, *args, **kw)

        return handler

    @staticmethod
    def _proxy_lines(pipe, handler: Callable):
        last = None
        with pipe:
            if handler:
                for line in pipe:
                    last = handler(line.decode().rstrip(), last=last)


class LazySubprocess(LazyLoad):
    """An Subprocess executed only when run/read/results are called."""

    def __init__(self, *args, **kw):
        super().__init__(Subprocess)
        self(*args, **kw)

    def run(self):
        return self.load(force=True)

    def read(self):
        return self.load().read()

    def results(self):
        return self.load().results()


class SubprocessPool(ThreadPoolExecutor):
    """A subprocess pool with a similar mode of operation to concurrent.futures."""

    def submit(self, *args, **kw):
        """Submits a subprocess to be executed."""
        p = LazySubprocess(*args, **kw)
        f = super().submit(p.results)
        f.external = p
        return f

    def map(self, cmds, timeout=None, **kw):
        if timeout is not None:
            end_time = timeout + time.monotonic()
        fs = [self.submit(cmd, **kw) for cmd in cmds]

        def result_iterator():
            try:
                fs.reverse()
                while fs:
                    if timeout is None:
                        yield fs.pop().result()
                    else:
                        yield fs.pop().result(end_time - time.monotonic())
            finally:
                for future in fs:
                    future.cancel()

        return result_iterator()
