import os
import shutil
import sys
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def embed(basedir: str = None):
    # Get base dir
    if not basedir:
        basedir = os.environ.get("SCHRODINGER", None)
        if not basedir:
            basedir = shutil.which("maestro")
            if basedir:
                basedir = Path(basedir).parent
            else:
                raise RuntimeError("module 'schrodinger' can not be embed, missing SCHRODINGER env var")
    basedir = Path(basedir).absolute()

    # Add paths for modules
    libdir = basedir / "internal" / "lib"
    moduledir = next(libdir.glob("python*")) / "site-packages"
    sys.path.append(str(moduledir))

    # Add dll paths for Windows
    if os.name == "nt":
        dlls = [basedir / "internal" / "bin"]
        dlls += list(basedir.glob("*/bin/Windows-x64"))
        for dll in dlls:
            os.add_dll_directory(dll)

    # Add env vars
    os.environ["SCHRODINGER_ALLOW_UNSAFE_MULTIPROCESSING"] = "1"

    try:
        yield
    finally:
        sys.path.remove(str(moduledir))
        del os.environ["SCHRODINGER_ALLOW_UNSAFE_MULTIPROCESSING"]
