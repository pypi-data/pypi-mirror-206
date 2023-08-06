from typing import Type, TypeVar, Generator, Optional

from schrodinger.structure import StructureReader, StructureWriter
from schrodinger.structure._io import count_structures

from .structure import Structure as _S

T = TypeVar("T", bound=_S)


def reader(f_path: str, index: int = 1, cls: Type[T] = _S, **kw) -> Generator[T, None, None]:
    with StructureReader(str(f_path), index=index) as reader:
        for st in reader:
            yield cls(st, **kw)


def read_one(f_path: str, index: int = 1, cls: Type[T] = _S, **kw) -> Optional[T]:
    try:
        return next(reader(str(f_path), index=index, cls=cls, **kw))
    except StopIteration:
        return None


def writer(f_path: str, **kw):
    return StructureWriter(str(f_path), **kw)


def write_one(st: _S, f_path: str, **kw):
    with writer(str(f_path), **kw) as f:
        f.append(st)
