import os
import shlex
from subprocess import PIPE, Popen
from typing import List, Union


def run(
    cmd: Union[List, str],
    cwd=None,
    inp: str = None,
    shell: bool = None,
    login=False,
    error=RuntimeError,
):
    if shell is None:
        shell = isinstance(cmd, str)
    if shell:
        if isinstance(cmd, List):
            cmd = shlex.join([str(c) for c in cmd])
        if login:
            cmd = f'{os.environ["SHELL"]} -l -c "{cmd}"'
    else:
        if isinstance(cmd, List):
            cmd = [str(c) for c in cmd]
        elif isinstance(cmd, str):
            cmd = shlex.split(cmd)
    p = Popen(cmd, shell=shell, cwd=cwd, stdout=PIPE, stderr=PIPE, stdin=PIPE if inp else None)
    out, err = p.communicate(inp.encode() if inp else None)
    if err and error:
        if issubclass(error, Exception):
            raise error(err.decode())
        elif isinstance(error, Exception):
            raise error
        elif isinstance(error, str):
            raise RuntimeError(error)
    return out.decode()
