def test_import():
    import zzlib
    from zzlib import cls, func, mixin, utils
    from zzlib.shell import env, envmgr, pathutils, sandbox, shell, slurm, subprocess
    from zzlib.log import logger, liblogger, forcelogger
    from zzlib.dl import device
    from zzlib.data import pandas
    from zzlib.cli import click, typer, progress
    from zzlib.bio import seq
