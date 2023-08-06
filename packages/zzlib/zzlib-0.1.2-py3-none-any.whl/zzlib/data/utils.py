from contextlib import contextmanager
from pathlib import Path


@contextmanager
def cacher(file: str, default=None):
    """
    Load variable from cachefile and save automatically when results of some
    time-consuming calculation are stored in this variable.
    """
    import joblib as jl

    if not Path(file).exists():
        obj = default
    else:
        obj = jl.load(file)
    yield obj
    jl.dump(obj, file)
