from itertools import product
from typing import List, Tuple, Type, TypeVar, Generator, Union

from ..func import flatten, rename_dup_in
from ..shell.pathutils import build_out_path
from .files import read_one, reader, writer, StructureWriter
from .structure import Structure as _S

T = TypeVar("T")


def workflow(*inputss: Union[str, List[str]], cls: Type[T] = _S, **kw) -> Generator[T, None, None]:
    """Iterate over (st_first, *st_others)."""
    for inputs in product(*[flatten(a) for a in inputss]):
        others = [read_one(i, cls=cls, **kw) for i in inputs[1:]]
        for st in reader(inputs[0], cls=cls, **kw):
            if others:
                yield st, *others
            else:
                yield st


def workflow_output_st(
    *inputss: Union[str, List[str]],
    out_path: str = None,
    use_title=True,
    ext: str = None,
    cls: Type[T] = _S,
    **kw,
) -> Generator[Tuple[StructureWriter, T], None, None]:
    """Iterate over (output_writer, st_first, *st_others), writer will be generated for each st."""
    for inputs in product(*[flatten(a) for a in inputss]):
        others = [read_one(i, cls=cls, **kw) for i in inputs[1:]]
        if use_title:
            titles = rename_dup_in([st.title for st in reader(inputs[0], **kw)])
        for i, st in enumerate(reader(inputs[0], cls=cls, **kw)):
            if use_title:
                out_path_guess = build_out_path(inputs[0], out_path=out_path, name=titles[i], ext=ext)
            else:
                out_path_guess = build_out_path(
                    inputs[0], out_path=out_path, suffix=i, suffix_mode="force", ext=ext
                )
            with writer(out_path_guess) as w:
                if others:
                    yield w, st, *others
                else:
                    yield w, st


def workflow_output_file(*inputss, out_path=None, ext=None, **kw):
    """Iterate over (output_writer, st_first, *st_others), writer will be generated for each file."""
    for inputs in product(*[flatten(a) for a in inputss]):
        others = [read_one(i, **kw) for i in inputs[1:]]
        with writer(build_out_path(inputs[0], out_path=out_path, ext=ext)) as w:
            for st in reader(inputs[0], **kw):
                if others:
                    yield w, st, *others
                else:
                    yield w, st
