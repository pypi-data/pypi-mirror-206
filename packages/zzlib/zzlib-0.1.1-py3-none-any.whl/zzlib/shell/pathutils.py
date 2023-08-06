from pathlib import Path
from typing import Iterable, List, Union

from ..func import flatten


def parse_input(input: Union[str, Path, Iterable], ext: str = None) -> List[Path]:
    """Parse a list of input path of dir or file to lists of files.

    Args:
        input: path or list of paths of input dirs or files.
        ext: extension to be searched in dirs, such as ".pdb". Defaults to None, meaning all dirs will be ignored.

    Returns:
        list of files or list of list of files, example:
        [
            [
               <file1.1 in dir1>
               <file1.2 in dir1>
            ],
            <file2>,
            [
               <file3.1 in dir3>
            ],
        ]
    """

    results = []
    if isinstance(input, Iterable):
        for f in input:
            f = Path(f)
            if f.is_file():
                results.append([f])
            elif f.is_dir() and ext:
                results.append(list(f.glob(f"*{ext}")))
            else:
                raise IOError(f'input files in: {", ".join(input)} are not found')
        if all(len(i) == 1 for i in results):
            return list(flatten(results))
    else:
        f = Path(input)
        if f.is_file():
            return [f]
        elif f.is_dir() and ext:
            return list(f.glob(f"*{ext}"))
        else:
            raise IOError(f"input files in: {input} are not found")


def build_out_path(in_path: str, out_path: str = None, name=None, suffix="", ext=None):
    """Build output filename based on input file and suffix.

    Args:
        in_path: the path of the processing file.
        out_path: the path of the output dir or path. Defaults to the dir path of in_path.
        name: the filename of the output file. Defaults to the filename of in_path.
        suffix: the suffix to be added to the file name of the output file.
        ext: the extension of the output file. Defaults to the extension of in_path.
    """
    in_path = Path(in_path)
    if not in_path.is_file():
        raise ValueError("in_path must be path to an existing file")
    if out_path:
        out_path = Path(out_path)
        if out_path.is_file():
            return out_path
        elif out_path.is_dir():
            out_dir = out_path
        else:
            return out_path
    else:
        out_dir = in_path.parent
    o_ext = "".join(in_path.suffixes)
    if not ext:
        ext = o_ext
    if not name:
        name = str(in_path.name).rstrip(o_ext)
    out_path = out_dir / (name + suffix + ext)
    return out_path.resolve()
