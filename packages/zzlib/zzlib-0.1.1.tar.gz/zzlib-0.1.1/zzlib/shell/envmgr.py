import json
import os
import random
import shlex
import string
import sys
from pathlib import Path as P
from typing import Dict, List, Type, Union

from ..func import to_iterable
from .subprocess import Subprocess, SubprocessError


class EnvMgr:
    """
    A class for saving, updating and running commands with environment variables

    Args:
        env: Additional environment variables for the environment.
        inherit: Copy all of the current environment variables to the environment.
                 Only functional when any env is set.
    """

    def __init__(self, env: Dict[str, str] = None, inherit=False, **kw):
        self.env = {}
        if inherit:
            self.env.update(os.environ)
        if env:
            self.env.update(env)
        self.kw = kw

    def run(
        self,
        *args,
        cls: Type[Subprocess] = Subprocess,
        env: Dict[str, str] = {},
        nokw=False,
        **kw,
    ):
        """Start a process in the envvar manager.

        Args:
            cls: Popen-like class to be used. Defaults to Subprocess.
            env: Extra environment variables to be passed. Defaults to {}.
            nokw: Do not use kws defined for the environment.
        """
        if not nokw:
            kw = {**self.kw, **kw}
        env.update(self.env if self.env else os.environ)
        return cls(*args, env=env, **kw)

    def shell(self, *args, shell: str = "bash", clean=False, **kw):
        """Start a command in the envvar manager in "shell mode".

        Args:
            shell: Shell exec name, such as 'bash', 'zsh', etc.
            clean: Run in a clean environment.
        """
        return self.run(*args, shell=shell, clean=clean, **kw)

    def update(self, cmd, fail="failed to update env from script", **kw):
        """Update the environment variables after running a command from shell.

        Args:
            cmd (str): A command to be run. Usually "source ..." or "... load" or "... activate".
        """
        dump = f'{sys.executable} -c "import os, json; print(json.dumps(dict(os.environ)))"'
        proc = self.shell(f"{cmd} 1>&2 && {dump}", stdout="pipe", nokw=True, **kw)
        proc.check(fail=fail)
        try:
            env = json.loads(proc.stdout.read())
        except json.JSONDecodeError:
            raise SubprocessError(f"failed to update env from script, invalid env.")
        self.env.update(env)

    def load(self, specs, **kw):
        raise NotImplementedError()


class LoadableEnvMgr(EnvMgr):
    """
    A class for running commands in a loadable environment.

    Args:
        env_sh: Init shell script to be sourced for loading environment.
    """

    load_cmd = None

    def __init__(self, env_sh: str = None, env: Dict[str, str] = None, inherit=False, **kw):
        super().__init__(inherit, env, **kw)
        env_sh = self.get_env_sh(env_sh)
        self.update(
            f"source {shlex.quote(str(env_sh))} >/dev/null",
            clean=True,
            fail=f"failed to load {self.name} init shell script",
        )

    def load(self, specs: Union[str, List[str]]):
        """Load specs into the environment."""
        if not self.load_cmd:
            raise NotImplementedError()
        spec_str = " ".join(shlex.quote(s) for s in to_iterable(specs))
        self.update(
            f"{self.load_cmd} {spec_str} >/dev/null",
            fail=f'failed to load {self.name} specs "{spec_str}"',
        )
        return self

    @property
    def name(self):
        return self.__class__.__name__.lower()

    def get_env_sh(self, env_sh: str):
        if not P(env_sh).is_file():
            msg = f'{self.name} init shell script "{env_sh}" is not found.'
            raise FileNotFoundError(msg)
        return env_sh


class Spack(LoadableEnvMgr):
    load_cmd = "spack load"

    def get_env_sh(self, env_sh: str):
        if not env_sh:
            if "SPACK_ROOT" in os.environ:
                env_sh = P(os.environ.get("SPACK_ROOT")).joinpath("share", "spack", "setup-env.sh")
            else:
                raise RuntimeError(
                    "spack init shell script can not be found automatically, and env_sh is not provided"
                )
        return super().get_env_sh(env_sh)


class Module(LoadableEnvMgr):
    load_cmd = "module load"

    def get_env_sh(self, env_sh: str):
        if not env_sh:
            if "MODULESHOME" in os.environ:
                env_sh = P(os.environ.get("MODULESHOME")).joinpath("init", "profile")
            else:
                raise RuntimeError(
                    "module init shell script can not be found automatically, and env_sh is not provided"
                )
        return super().get_env_sh(env_sh)


class Venv(LoadableEnvMgr):
    """
    A class for running commands in a vitualvenv environment.

    Args:
        env_sh: Path of the venv, or activate script of the venv. Create if not exists.
    """

    load_cmd = "pip --disable-pip-version-check install -U"

    def get_env_sh(self, env_sh: str):
        if not env_sh:
            raise ValueError("venv path must be provided")
        if not P(env_sh).exists():
            from venv import EnvBuilder

            EnvBuilder(with_pip=True, prompt=".").create(env_sh)
        if P(env_sh).is_dir():
            env_sh = P(env_sh).joinpath("bin", "activate")
        return super().get_env_sh(env_sh)


class Conda(LoadableEnvMgr):
    load_cmd = 'eval "$(conda shell.bash hook)" && conda activate'

    def __init__(self, env_sh: str = None, env: Dict[str, str] = None, inherit=False, **kw):
        super().__init__(env_sh, env, inherit, **kw)

    def get_env_sh(self, env_sh: str):
        if not env_sh:
            if "CONDA_EXE" in os.environ:
                env_sh = P(os.environ.get("CONDA_EXE")).parent.parent.joinpath("etc", "profile.d", "conda.sh")
            else:
                raise RuntimeError("conda can not be found automatically, and env_sh is not provided")
        return super().get_env_sh(env_sh)
