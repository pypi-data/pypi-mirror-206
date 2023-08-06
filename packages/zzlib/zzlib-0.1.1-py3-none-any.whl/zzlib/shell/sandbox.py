from pathlib import Path as P
from tempfile import TemporaryDirectory
from typing import List
import shutil

from funcy.seqs import count


class Sandbox:
    """
    A context that creates a temporary directory emulating the directory structure of specific paths.

    Args:
        basedir: location for sandbox tempdir creation and default value for cwd.
        keep: keep the sandbox tempdir.
    """

    def __init__(self, basedir: P = None, keep: bool = False, link=None):
        self._basedir = P(basedir).absolute()
        self._keep = keep
        if link is None:
            link = True if basedir else False
        self._link = link
        self._temp = None
        self._watching = {}

    def __enter__(self):
        self._temp = TemporaryDirectory(dir=self._basedir, prefix=".sandbox-")
        if self._link:
            self.add(self._basedir, to=".", recursive=True)
        return self

    def __exit__(self, type, value, trace):
        if self._temp and not self._keep:
            self._temp.cleanup()

    def __call__(self, relpath: P):
        if P(relpath).is_absolute():
            raise ValueError("path must be relative")
        if not self.loc:
            raise FileNotFoundError(f"can not operate on a pending sandbox")
        return self.loc / relpath

    __truediv__ = __getitem__ = __call__

    @property
    def loc(self):
        if self._temp:
            return P(self._temp.name)

    def add(self, path: P, recursive=True, to: P = None, copy=False, overwrite=False):
        path = P(path) if P(path).is_absolute() else self._basedir / path
        to = to or path.name
        if path.is_dir() and recursive:
            return self.add_glob("**/*", cwd=path, to=to, copy=copy)
        elif path.is_file():
            self._mig(self.loc / to, path.absolute(), copy=copy, overwrite=overwrite)
            return 1
        else:
            return 0

    def copy(self, path: P, recursive=True, to: P = None, overwrite=False):
        return self.add(path, recursive=recursive, to=to, copy=True, overwrite=overwrite)

    def add_glob(
        self,
        glob: str,
        copy=False,
        overwrite=False,
        depth: int = None,
        cwd: P = None,
        to: P = None,
        ignore: List[str] = [],
    ):
        cwd = P(cwd).absolute() if cwd else self._basedir
        globpath = P(glob) if P(glob).is_absolute() else P(cwd) / glob
        if not globpath.resolve().is_relative_to(cwd):
            raise ValueError("base must be a parent of glob")
        ops = {}
        for f in P("/").glob(str(globpath.relative_to("/"))):
            relative = f.relative_to(cwd)
            if depth is not None:
                d = len(relative.parents)
                if d > depth:
                    continue
                elif d < depth and f.is_file():
                    continue
            elif f.is_dir():
                continue
            if any(relative.match(g) for g in ignore):
                continue
            if to:
                relative = P(to) / relative
            link = self.loc / relative
            ops[link] = f
        for link, f in ops.items():
            self._mig(link, f, copy=copy, overwrite=overwrite)
        return len(ops)

    def copy_glob(
        self,
        glob: str,
        overwrite=False,
        depth: int = None,
        cwd: P = None,
        to: P = None,
        ignore: List[str] = [],
    ):
        return self.add_glob(
            glob,
            overwrite=overwrite,
            depth=depth,
            cwd=cwd,
            to=to,
            ignore=ignore,
            copy=True,
        )

    def _mig(self, to: P, src: P, copy=False, overwrite=False, forward=True):
        while True:
            try:
                if not copy:
                    to.symlink_to(src)
                else:
                    if to.is_file() and not to.is_symlink():
                        raise FileExistsError(to)
                    try:
                        shutil.copy(src, to)
                    except IsADirectoryError:
                        shutil.copytree(src, to)
                    if forward:
                        self._watching[to] = src
                break
            except FileNotFoundError:
                to.parent.mkdir(parents=True, exist_ok=True)
            except shutil.SameFileError:
                to.unlink(missing_ok=True)
            except FileExistsError:
                if overwrite:
                    to.unlink(missing_ok=True)
                else:
                    for i in count(1):
                        try:
                            to.rename(to.with_stem(f"{to.stem}#{i}"))
                            break
                        except FileExistsError:
                            pass

    def results(self, glob: str = "**/*"):
        if not self.loc:
            raise FileNotFoundError(f"can not operate on a pending sandbox")
        for f in self.loc.glob(glob):
            if (not f.is_symlink()) and (not f.is_dir()):
                yield f

    def retrive(self, path: P = None, to: P = None):
        if not path:
            return self.retrive_glob(glob="**/*")
        else:
            path = self[path]
            if not to:
                to = self._basedir / (path.relative_to(self.loc))
            return self._mig(to, path, copy=True, overwrite=True, forward=False)

    def retrive_glob(self, glob: str, overwrite=True):
        ops = 0
        for f in self.results(glob):
            to = self._watching.get(f, self._basedir / (f.relative_to(self.loc)))
            self._mig(to, f, copy=True, overwrite=overwrite, forward=False)
            ops += 1
        return ops
