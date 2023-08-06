import warnings
from typing import Iterable, TypeVar, Generator

from ..func import is_in_notebook, to_iterable

T = TypeVar("T")


def _rich_get_detailed_process(**kw):
    from rich.progress import Progress, TextColumn

    return Progress(
        *Progress.get_default_columns(),
        TextColumn("{task.completed}/{task.total}"),
        **kw,
    )


def _rich_progress(iter: Iterable, desc=None, total=None, progress=None):
    if not total:
        try:
            total = len(iter)
        except TypeError:
            raise ValueError("length must be provided for non-lists") from None
    if not progress:
        progress = _rich_get_detailed_process(transient=True)
    with progress as p:
        task = p.add_task(f"{desc.capitalize()} ..." if desc else "", total=total)
        for i in iter:
            p.advance(task)
            yield i


def progress(iter: Iterable[T], desc=None, total=None, by=("rich", "tqdm"), **kw) -> Generator[T, None, None]:
    for b in to_iterable(by):
        try:
            if b == "rich":
                if not is_in_notebook():
                    return _rich_progress(iter, desc=desc, total=total, **kw)
            elif b == "tqdm":
                from tqdm import tqdm

                return tqdm(iter, desc=desc, total=total, **kw)
        except ImportError:
            pass
    else:
        warnings.warn(f'Process bar is disabled due to lack of "{by}" lib.')
