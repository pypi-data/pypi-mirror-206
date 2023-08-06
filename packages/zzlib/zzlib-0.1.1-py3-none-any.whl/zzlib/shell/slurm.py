from __future__ import annotations

import re
import shlex
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from datetime import datetime, timedelta
from enum import Enum, EnumMeta
from functools import partial
from inspect import currentframe, getmodulename
from io import StringIO
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Callable, Iterable, List, Set, Union

import numpy as np
import pandas as pd
from appdirs import user_cache_dir

from ..cls import Def, Proxy
from ..func import to_iterable
from ..log import forcelogger, liblogger
from ..mixin import StopableMixin
from ..utils import Eventer, EventSource, Logger, LoggerPattern, TimedCache
from .shell import run

# Pipes
TMPLOG = -1
DEVNULL = -3


# Errors
class SlurmError(RuntimeError):
    pass


class SlurmJobError(SlurmError):
    pass


class SlurmCommandError(SlurmError):
    pass


# Helpers
run = partial(run, error=SlurmCommandError)


def parse_host_spec(spec):
    return run(f"scontrol show hostnames {shlex.quote(spec)}").strip().split("\n")


# Enums
class JobEvent(Enum):
    IN_QUEUE = 10
    STARTED = 20
    FINISHED = 30
    OK = 31
    FAILED = 32


class _JobStateMeta(EnumMeta):
    def __getitem__(self, item):
        if isinstance(item, str):
            item = item.split()[0].upper()
        if item not in self.__members__:
            item = "UNKNOWN"
        return super().__getitem__(item)


class JobState(Enum, metaclass=_JobStateMeta):
    NOT_FOUND = 0
    PENDING = 10
    SUSPENDED = 11
    REQUEUED = 12
    RESIZING = 13
    RUNNING = 20
    COMPLETED = 30
    CANCELLED = 40
    FAILED = 41
    DEADLINE = 42
    TIMEOUT = 43
    OUT_OF_MEMORY = 44
    NODE_FAIL = 45
    BOOT_FAIL = 46
    PREEMPTED = 47
    REVOKED = 48
    UNKNOWN = 50

    def is_in_queue(self):
        return 0 < self.value < 30

    def is_running(self):
        return 20 <= self.value < 30

    def is_finished(self):
        return self.value >= 30

    def is_ok(self):
        return 30 <= self.value < 40

    def is_failed(self):
        return self.value >= 40


# Consts
LOG_INFO_PROMPT = "#>> "


# Classes
class JobScript:
    def __init__(
        self,
        script: str,
        shell=Def,
        name: str = Def,
        caller: str = Def,
        nodes: int = Def,
        nodelist: Union[List, str] = Def,
        cpus: int = Def,
        gpus: int = Def,
        partition: str = Def,
        begin: Union[datetime, str] = Def,
        array: Union[List, str] = Def,
        stdout: str = Def,
        stderr: str = Def,
        info=True,
        monitor=True,
        **kw,
    ):
        # 获得调用模块并计算默认任务名
        self.caller = caller or getmodulename(currentframe().f_back.f_code.co_filename)
        if Path(script).is_file():
            with open(script) as f:
                script = f.read()
            self.name = name or self.caller + "%" + Path(script).stem
        else:
            self.name = name or self.caller + "%" + datetime.now().strftime("%b%d")
        # 准备 lines
        exec_line, arg_lines, cmd_lines = self._prep_lines(script)
        # 处理 shell
        if shell:
            exec_line = f"#!{shell}"
        elif not exec_line:
            exec_line = "#!/bin/bash"
        # 解析输入值
        if isinstance(nodelist, Iterable):
            nodelist = ",".join(nodelist)
        if isinstance(array, Iterable):
            array = ",".join(str(i) for i in array)
        if isinstance(begin, timedelta):
            begin = datetime.now() + begin
        if isinstance(begin, datetime):
            begin = begin.strftime("%Y-%m-%dT%H:%M:%S")
        # 增加 sbatch 参数
        mod_arg = partial(self._mod_arg, lines=arg_lines)
        mod_arg(["--job-name=", "-J"], name, self.name)
        mod_arg(["--nodes=", "-N"], nodes, len(parse_host_spec(nodelist)))
        mod_arg(["--nodelist=", "-w"], nodelist)
        mod_arg(["--cpus-per-task=", "-c"], cpus, 1)
        mod_arg(["--gres=gpu:"], gpus)
        mod_arg(["--partition=", "-p"], partition, "gpu" if gpus else "cpu")
        mod_arg(["--begin=", "-b"], begin)
        mod_arg(["--output=", "-o"], stdout, "/dev/null")
        mod_arg(["--error=", "-e"], stderr, "/dev/null")
        mod_arg(["--array=", "-a"], array)
        for k, v in kw.items():
            mod_arg([k], v)
        # 增加特定的命令
        if monitor:
            cmd_lines[0:0] = self._monitor_cmd_lines
        if info:
            cmd_lines[0:0] = self._info_cmd_lines
        # 合并 lines
        self.content = "\n".join([exec_line] + arg_lines + cmd_lines)

    @staticmethod
    def _prep_lines(script: str):
        lines = script.strip().split("\n")
        exec_line = lines[0] if lines[0].startswith("#!") else None
        arg_lines = []
        cmd_lines = []
        arg_flag = True
        for l in lines[1 if exec_line else 0 :]:
            if arg_flag and l.startswith(f"#SBATCH "):
                arg_lines.append(l)
            elif arg_flag or l.strip():
                cmd_lines.append(l.rstrip())
                arg_flag = False
        return exec_line, arg_lines, cmd_lines

    @staticmethod
    def _mod_arg(args: Iterable, value, default=None, lines: List[str] = []):
        for i, l in enumerate(lines):
            for a in args:
                if l.startswith(f"#SBATCH {a}"):
                    if not value:
                        return False
                    else:
                        lines[i] = f'#SBATCH {args[0]}"{value}"'
                        return True
        else:
            value = value or default
            if value:
                lines.append(f'#SBATCH {args[0]}"{value}"')
                return True
            else:
                return False

    @property
    def _info_cmd_lines(self):
        lines = """
            if [ "$SLURM_ARRAY_TASK_ID" -eq "$SLURM_ARRAY_TASK_MIN" ]; then
                echo "{prompt}Job $SLURM_JOB_NAME ($SLURM_JOB_ID) is started at $(date +"%Y/%m/%d %T")."
                echo "{prompt}Job is running on $(hostname) with $SLURM_CPUS_ON_NODE cpus."
                echo "{prompt}Job is submited from $SLURM_SUBMIT_HOST at '$(basename "$SLURM_SUBMIT_DIR")' (usage $({usage}))"
            fi
        """.format(
            prompt=LOG_INFO_PROMPT,
            usage='grep "cpu " "/proc/stat" | awk \'{usage=($2+$4)*100/($2+$4+$5)} END {print usage "%"}\'',
        ).split(
            "\n"
        )
        return (l.strip() for l in lines)

    @property
    def _monitor_cmd_lines(self):
        # TODO: 实现代码
        return []

    def __repr__(self):
        return f"<Script for {self.name} at {hex(id(self))}>"


class JobEventer(Eventer):
    def __init__(self, job: Job):
        self.job = job
        super().__init__(
            EventSource(self.job.is_finished).add(JobEvent.FINISHED),
            EventSource(self.job.is_running).add(JobEvent.STARTED),
            EventSource(self.job.is_in_queue).add(JobEvent.IN_QUEUE),
            interval=self.job.interval,
        )
        self._started_flag = self.event_flag(JobEvent.STARTED)
        self.add_callback(self._check_after_finished, events=JobEvent.FINISHED)

    def __getitem__(self, key):
        for s in self.sources:
            if s.func == key:
                return s
        else:
            raise KeyError(key)

    def set_state(self, in_queue=False, running=False, finished=False):
        if in_queue is not None:
            self[self.job.is_in_queue].value = in_queue
        if running is not None:
            self[self.job.is_running].value = running
        if finished is not None:
            self[self.job.is_finished].value = finished

    def wait(self, events=JobEvent.FINISHED, timeout=None):
        events = to_iterable(events)
        if self.job.exists():
            if JobEvent.STARTED in events and self.job.is_running():
                return True
            if self.job.is_finished():
                if JobEvent.FINISHED in events:
                    return True
                if JobEvent.OK in events and self.job.is_ok():
                    return True
                if JobEvent.FAILED in events and not self.job.is_ok():
                    return True
        return super().wait(events, timeout=timeout)

    def _check_after_finished(self, events):
        if not self._started_flag.is_set():
            yield JobEvent.STARTED
        if self.job.is_ok():
            yield JobEvent.OK
        else:
            yield JobEvent.FAILED


class Job:
    def __init__(
        self,
        arg: Union[JobScript, str],
        stdout=Def,
        stderr=Def,
        cwd: str = None,
        interval: float = 1.0,
        **kw,
    ):
        if re.match(r"(\d+)(?:_(\d+))?", str(arg)):
            self.id = str(arg)
            self.script = None
        else:
            self.id = None
            if isinstance(arg, JobScript):
                self.script = arg
            else:
                caller = getmodulename(currentframe().f_back.f_code.co_filename)
                self.script = JobScript(arg, caller=caller, **kw)
        self.cwd = cwd
        self.interval = Proxy(interval)
        self.eventer = JobEventer(self)
        self.logger = JobLogger(self)
        self._info = TimedCache(self._get_info, timeout=self.interval, onupdate=self.eventer.check)
        self._running_info = TimedCache(self._get_running_info, timeout=self.interval)
        self._stdout = self._use_std(stdout)
        self._stderr = self._use_std(stderr)

    # == Operations ==
    def submit(self, depends=(), check_depends=True, valid=True):
        if self.id:
            raise SlurmJobError(f"this job has been assigned id {self.id}, please recreate job to rerun")
        if not self.script:
            raise SlurmJobError("this job has not been prepared with a script")
        stdout_args = f" -o {self._stdout}" if self._stdout else ""
        stderr_args = f" -e {self._stderr}" if self._stderr else ""
        if check_depends:
            for j in depends:
                if not isinstance(j, Job):
                    j = Job(j)
                if not j.exists():
                    raise SlurmJobError(f"job dependency {j.id} does not exist")
        dep_args = f' -d afterok:{":".join(j.id for j in depends)}' if depends else ""
        out = run(
            f"sbatch{stdout_args}{stderr_args}{dep_args}",
            inp=self.script.content,
            cwd=self.cwd,
        )
        match = re.search(r"\s(\d+)\s", out)
        if match:
            self.id = match.group(1)
            liblogger.info(f"Submitted job and got id {self.id}.")
        else:
            raise SlurmCommandError("error during submitting slurm job")
        self.eventer.set_state()
        if valid:
            liblogger.info(f"Waiting for the job to exist after submitting.")
            with self._enhanced_refresh():
                if not self.wait(JobEvent.IN_QUEUE, timeout=30):
                    raise SlurmCommandError(
                        f"timeout waiting for submitted slurm job {self.id} to be in queue"
                    )
            liblogger.info(f"Found the job in queue, finished submitting.")
        return self

    def cancel(self, missing_ok=True):
        if (not missing_ok) and (not self.is_in_queue()):
            raise SlurmJobError(f"this job is not in queue")
        run(f"scancel {self.id}")

    def suspend(self):
        run(f"scontrol suspend {self.id_or()}")

    def release(self):
        run(f"scontrol release {self.id_or()}")

    def wait(self, events=JobEvent.FINISHED, timeout=None):
        return self.eventer.wait(events, timeout=timeout)

    def start_logger(self, *args, wait=True, **kw):
        if not self.is_finished():
            return self.logger.configure(*args, **kw).start(wait=wait)

    # == Informations ==

    def __getitem__(self, key):
        return Job(f"{self.id}_{key}")

    def tasks(self):
        indexes = self.info().index
        if len(indexes) == 1:
            yield self
        else:
            for i in indexes:
                yield self[i]

    def id_or(self, oper="fail"):
        if not self.id:
            if oper == "fail":
                raise SlurmJobError("this job has not been assigned a job id")
            else:
                return oper
        else:
            return self.id

    def info(
        self,
        key: Union[str, Iterable[str]] = None,
        default=Def,
        task: Union[int, Iterable[int]] = None,
        unique=True,
        running=False,
        modifier: Callable = None,
        forceupdate=False,
        noupdate=False,
    ):
        df = self._info.updated(forceupdate, noupdate)
        if running:
            running_info = self._running_info.updated(forceupdate, noupdate)
            df = df.merge(
                running_info,
                how="outer",
                left_index=True,
                right_index=True,
                suffixes=("", "_running"),
            )
        if not len(df):
            if default is Def:
                raise SlurmJobError(f'this job ({self.id_or("Unknown")}) does not exist')
        if not key:
            key = df.columns
        if not task:
            task = df.index
        if default is Def:
            view = df.loc[task, :].get(key, default)
        else:
            view = df.loc[task, :].get(key)
        if unique and isinstance(view, pd.Series):
            if (view == view.iloc[0]).all():
                view = view.iloc[0]
        if modifier:
            if isinstance(view, pd.Series):
                view = view.apply(modifier)
            else:
                view = modifier(view)
        return view

    @property
    def state(self):
        def _modifier(v):
            return JobState[v]

        return self.info("State", modifier=_modifier)

    @property
    def name(self):
        def _modifier(v):
            if v == "allocation" or not v:
                return self.script.name if self.script else "Unknown"
            return v

        return self.info("JobName", modifier=_modifier)

    @property
    def nodes(self):
        def _modifier(v):
            if v:
                return parse_host_spec(v)
            else:
                return ()

        return self.info("NodeList", modifier=_modifier)

    @property
    def elapsed(self):
        def _modifier(v):
            return timedelta(seconds=int(v))

        return self.info("ElapsedRaw", modifier=_modifier)

    @property
    def stdout(self):
        f = self._stdout or self.info("StdOut", running=True)
        if f and f != "/dev/null":
            return JobLogfile(f, job=self)

    @property
    def stderr(self):
        f = self._stderr or self.info("StdErr", running=True)
        if f and f != "/dev/null":
            return JobLogfile(f, job=self)

    def exists(self):
        try:
            self.info()
        except SlurmJobError:
            return False
        else:
            return True

    def is_in_queue(self):
        state = self.state
        if isinstance(state, pd.Series):
            return any(s.is_in_queue() for s in state)
        else:
            return state.is_in_queue()

    def is_finished(self):
        state = self.state
        if isinstance(state, pd.Series):
            return any(s.is_finished() for s in state)
        else:
            return state.is_finished()

    def is_ok(self):
        if self.is_in_queue():
            raise SlurmJobError("this job is still running")
        exitcode = self.info("ExitCode", None)
        if exitcode is None:
            return False
        if int(exitcode.split(":")[0]) > 0:
            return False
        if self.state != JobState.COMPLETED:
            return False
        return True

    def is_running(self):
        state = self.state
        if isinstance(state, pd.Series):
            return any(s.is_running() for s in state)
        else:
            return state.is_running()

    # == Private Functions ==

    @contextmanager
    def _enhanced_refresh(self, multiply=5):
        liblogger.trace(f"Job update interval is set {multiply}x")
        self.interval = self.interval / multiply
        try:
            yield self.interval
        finally:
            liblogger.trace(f"Job update interval is restored.")
            self.interval = self.interval * multiply

    def _get_info(self):
        def _split_jobid(row):
            match = re.match(r"(\d+)(?:_(\d+))?", str(row["JobID"]))
            if not match:
                return row
            jid, tid = match.groups()
            row["JobIDBase"] = int(jid) if jid else np.nan
            row["ArrayTaskId"] = int(tid) if tid else np.nan
            return row

        out = run(f"sacct -j {self.id_or()} -X -P --format all").strip()
        try:
            df = pd.read_csv(StringIO(out), delimiter="|")
            df = df.replace(["Unknown"], np.nan)
            if len(df) > 0:
                df = df.apply(_split_jobid, axis=1)
                df = df.set_index("ArrayTaskId")
        except Exception as e:
            raise SlurmCommandError(f'output from "sacct" command is abnormal: {e}') from None
        liblogger.trace("Job information refreshed.")
        return df

    def _get_running_info(self):
        out = run(f"scontrol show job {self.id_or()}", error=None).strip().split("\n\n")
        if not out:
            return pd.DataFrame()
        try:
            records = []
            for block in out:
                record = {}
                for i in re.findall("(?<![=\w])[^\s=]+=[^\s=]+(?![=\w])", block):
                    k, v = i.split("=")
                    if v in ("N/A", "None", "(null)"):
                        v = np.nan
                    record[k] = v
                records.append(record)
            df = pd.DataFrame(records)
            if "ArrayTaskId" not in df.columns:
                df["ArrayTaskId"] = np.nan
            else:
                df["ArrayTaskId"] = df["ArrayTaskId"].astype(int)
            df = df.set_index("ArrayTaskId")
        except Exception as e:
            raise SlurmCommandError(f'output from "scontrol" command is abnormal: {e}') from None
        liblogger.trace("Job running-related information refreshed.")
        return df

    @staticmethod
    def _use_std(std):
        if isinstance(std, JobLogfile):
            return std.path
        if not std:
            return None
        if std == DEVNULL:
            return Path("/dev/nul")
        if std == TMPLOG:
            return JobLogfile().path
        return Path(std).absolute()

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Job):
            return self.id == other.id
        return False

    def __repr__(self):
        if self.id:
            spec = f"Job {self.id}"
        else:
            if self.script:
                spec = "Prepared Job"
                spec += f" ({self.script.name})"
            else:
                spec = "Unprepared Job"
        return f"<{spec} at {hex(id(self))}>"


class JobLogfile(StopableMixin):
    spool = Path(user_cache_dir()) / "job_spool"

    def __init__(self, path: str = None, job: Job = None):
        super().__init__()
        if not path:
            self.spool.mkdir(exist_ok=True)
            with NamedTemporaryFile(dir=self.spool) as tmp:
                path = tmp.name
        self.path = Path(path).absolute()
        self.job = job

    def exists(self):
        return self.path.is_file()

    def remove(self):
        self.path.unlink(missing_ok=True)

    def follow(self, start=JobEvent.STARTED):
        if start:
            self.job.wait(start)
        liblogger.info(f'Logfile "{self.path.name}" is now followed.')
        with open(self.path) as f:
            line = ""
            while self.exists():
                tmp = f.readline()
                if tmp:
                    line += tmp
                    if line.endswith("\n"):
                        yield line.strip("\n")
                        line = ""
                else:
                    if self.job.is_finished():
                        for line in f.readlines():
                            yield line.strip("\n")
                        break
                    time.sleep(0.1)

    def results(self, **kw):
        return tuple(l for l in self.follow(**kw) if not l.startswith(LOG_INFO_PROMPT))

    def __repr__(self):
        spec = f'Logfile at "{self.path.name}"'
        if self.exists():
            spec += " (created)"
        return f"<{spec} at {hex(id(self))}>"


class JobLogger(Logger):
    DEFAULT_INFO_EVENTS = (JobEvent.STARTED, JobEvent.OK, JobEvent.FAILED)
    STARTED_INFO_SENT = object()

    def __init__(self, job: Job):
        super().__init__()
        self.job = job

    @staticmethod
    def _logfile_follow_wait(logfile: JobLogfile, info=True):
        if not logfile.job.is_running():
            if info:
                logfile.job.wait(JobLogger.STARTED_INFO_SENT)
            else:
                logfile.job.wait(JobEvent.STARTED)
        yield from logfile.follow(start=None)

    def configure(self, out="info", err="error", info="warning", monitor="debug"):
        if info is not None:
            self.sources[self._info_stream()] = self._get_pattern(info)
        if out is not None and self.job.stdout:
            self.sources[self._logfile_follow_wait(self.job.stdout, info is not None)] = self._get_pattern(
                out
            )
        if err is not None and self.job.stderr:
            self.sources[self._logfile_follow_wait(self.job.stderr, info is not None)] = self._get_pattern(
                err
            )
        return self

    @staticmethod
    def _get_pattern(arg, **kw):
        if isinstance(arg, LoggerPattern):
            return arg
        if isinstance(arg, str):
            func = getattr(forcelogger, arg)
        elif callable(arg):
            func = arg
        else:
            raise TypeError("get pattern can only be called with a LoggerPattern, Function or String")
        return LoggerPattern().add(func, **kw)

    def _info_stream(self, events=DEFAULT_INFO_EVENTS):
        for e in self.job.eventer.events(history=False):
            if events and e not in events:
                continue
            if e == JobEvent.STARTED:
                yield f"Job started on {self.job.nodes}."
                self.job.eventer.put(self.STARTED_INFO_SENT)
            elif e == JobEvent.OK:
                yield "Job finished successfully."
                break
            elif e == JobEvent.FAILED:
                yield f"Job failed."
                break


class JobPool:
    def __init__(self, interval=1.0):
        self.jobs = {}
        self.interval = Proxy(interval)
        self._submitter = ThreadPoolExecutor()
        self._submitter_futures = []
        self._running_jobids = TimedCache(self._get_running, timeout=self.interval)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return self._submitter.shutdown(wait=True)

    def _add_job(self, future):
        job: Job = future.result()
        self.jobs[job.id_or()] = job

    def submit(self, *args, depends=(), **kw):
        f = self._submitter.submit(Job(*args, **kw).submit, depends)
        self._submitter_futures.append(f)
        f.add_done_callback(self._add_job)
        return f

    def as_completed(self):
        while self.jobs or not all(task.done() for task in self._submitter_futures):
            for jid in set(self.jobs) - self._running_jobids:
                job = self.jobs[jid]
                del self.jobs[jid]
                yield job
            else:
                time.sleep(float(self.interval))

    def _get_running(self):
        liblogger.trace("List of running jobs refreshed.")
        return set(run("squeue -h -o %i").strip().split("\n"))

    def __repr__(self):
        return f"<Job Monitor ({len(self.jobs)} jobs) at {hex(id(self))}>"
