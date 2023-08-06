import ctypes
import itertools
from contextlib import contextmanager
from functools import reduce
from pathlib import Path
from threading import Lock
from typing import Any, Iterable, Type, Union, get_type_hints

from funcy import rpartial
from funcy.decorators import decorator, arggetter, get_argnames


def truncate_str(text: str, length: int):
    """Truncate a str to a certain length, and the omitted part is represented by "..."."""
    return f"{text[:length + 3]}..." if len(text) > length else text


def truncate_path(f: str, length: int):
    """Truncate a path str to a certain length, and the omitted part is represented by "..."."""
    if Path.cwd() in Path(f).parents:
        return "./" + str(Path(f).relative_to(Path.cwd()))
    else:
        result = Path(*Path(f).parts[-length:])
        if result.is_absolute():
            return str(result)
        else:
            return ".../" + str(result)


def remove_prefix(text: str, prefix: str):
    """Remove prefix from the begining of test."""
    return text[text.startswith(prefix) and len(prefix) :]


def get_after_char(text: str, delim: str):
    """Get characters after the first occurence of delim."""
    return text[text.index(delim) + len(delim) :]


def suffix_dup(l: Iterable[str]):
    """Rename duplicated names in a list with increasing suffixes."""
    results = []
    for i, v in enumerate(l):
        totalcount = l.count(v)
        count = l[:i].count(v)
        results.append(f"{v}_{str(count + 1)}" if totalcount > 1 else v)
    return results


def walk(l: Iterable[Iterable]):
    """Iterate over a irregular n-dimensional list."""
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


def flatten(l: Iterable[Union[Iterable, Any]]):
    """Flatten a irregular n-dimensional list to a 1-dimensional list."""
    return type(l)(walk(l))


def flatten2(l: Iterable[Iterable]):
    """Flatten a 2-dimensional list to a 1-dimensional list."""
    return list(itertools.chain.from_iterable(l))


def chain_decos(*decos):
    """A decorator that allows us to chain multiple decorators."""

    def deco(f):
        for deco in reversed(decos):
            f = deco(f)
        return f

    return deco


def in_range(t: Iterable, v):
    """Check value is in range of [a, b]."""
    if len(t) != 2:
        raise ValueError("range must be a iterable with 2 elements")
    try:
        import pandas as pd

        if pd.isnull(v):
            return False
    except ImportError:
        if v is None:
            return False
    if t[0] is not None and v < t[0]:
        return False
    if t[1] is not None and v > t[1]:
        return False
    return True


def is_in_notebook():
    """Check the script is run in jupyter notebook."""
    try:
        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        elif shell == "TerminalInteractiveShell":
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False  # Probably standard Python interpreter


def count(iter: Iterable):
    """Count total item number of an iterator."""
    return sum(1 for _ in iter)


def has_len(iter: Iterable, min_len: int = None):
    """Check if an iterator has items more than min_len."""
    for _ in range(min_len):
        try:
            _ = next(iter)
        except StopIteration:
            return False
    return True


def class_path(c: Type) -> str:
    """Return full path of a class."""
    module = c.__module__
    if module == "builtins":
        return c.__qualname__  # avoid outputs like 'builtins.str'
    return module + "." + c.__qualname__


def rename_dup_in(l: Iterable[str]):
    """Rename duplicated names in a list with increasing suffixes from 1."""
    results = []
    for i, v in enumerate(l):
        totalcount = l.count(v)
        count = l[:i].count(v)
        results.append(v + "_" + str(count + 1) if totalcount > 1 else v)
    return results


def product_nested(l: Iterable):
    """Product an irregular 2-dimensional list."""
    return itertools.product(*[i if isinstance(i, list) else [i] for i in l])


def split_kw(kw: dict, keys: Iterable, drops: Iterable = ()):
    """Split kw into filtered and others by specifying keys."""
    filtered = {}
    others = {}
    for k, v in kw.items():
        if k in keys:
            filtered[k] = v
        elif k not in drops:
            others[k] = v
    return filtered, others


def to_iterable(var: Union[Iterable, Any]):
    """Convert the value into a list if it is not an Iterable."""
    if var is None:
        return []
    if isinstance(var, str) or not isinstance(var, Iterable):
        return [var]
    else:
        return var


def to_exception(var: Union[Exception, str, Type[Exception]], default=RuntimeError):
    """Convert the value into a error when specifying error message, Exception or Exception instance."""
    if isinstance(var, str):
        return default(var)
    elif callable(var):
        return var()
    else:
        return var


@contextmanager
def nonblocking(lock: Lock):
    """Try to acquire the lock, if the lock is already acquired by other threads, ."""
    locked = lock.acquire(False)
    try:
        yield locked
    finally:
        if locked:
            lock.release()


def async_raise(tid, exception):
    ret = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.py_object(exception))
    if ret == 0:
        raise ValueError("invalid thread ID {}".format(tid))
    elif ret > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def get_tid(thread):
    import threading

    for tid, tobj in threading._active.items():
        if tobj is thread:
            return tid


def pipeline(*steps):
    return reduce(lambda x, y: y(x), list(steps))


class ConvertError(TypeError):
    pass


@decorator
def convert(call, *, force=False):
    """A decorator that convert type of args to its hinted type."""
    argvf = rpartial(arggetter(call._func), call._args, call._kwargs)
    argv = {n: argvf(n) for n in get_argnames(call._func)}
    argt = get_type_hints(call._func)
    for n, t in argt.items():
        v = argv[n]
        if hasattr(t, "__origin__"):
            if t.__origin__ == Union:
                ne = not isinstance(v, t.__args__)
                t = t.__args__[0]
            else:
                ne = not isinstance(v, t)
                t = t.__origin__
        else:
            ne = not isinstance(v, t)
        if ne:
            try:
                argv[n] = t(v)
            except:
                if force:
                    raise ConvertError(f"failed to convert {v} into {t}")
    return call._func(**argv)
