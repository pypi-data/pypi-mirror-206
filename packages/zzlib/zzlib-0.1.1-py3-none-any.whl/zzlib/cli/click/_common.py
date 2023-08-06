import click as _base


def inputs(*args, argument=False, required=True, multiple=True):
    """Decorator for adding a input option/argument, allowing files or dirs.

    Args:
        argument (bool, optional): Add an argument instead of option. Defaults to False.
        required (bool, optional): Defaults to True.
        multiple (bool, optional): If False, allow only one file. Defaults to True.
    """
    if not argument:
        args = args if args else ["--input", "-i"]
        return _base.option(
            *args,
            required=required,
            multiple=multiple,
            type=_base.Path(dir_okay=multiple, exists=True, readable=True),
            help="Input file/dir containing structures.",
        )
    else:
        nargs = -1 if multiple else 1
        args = args if args else ["input"]
        return _base.argument(
            "input",
            nargs=nargs,
            type=_base.Path(dir_okay=multiple, exists=True, readable=True),
        )


def outputs():
    """Decorator for adding a output option."""
    return _base.option(
        "--output",
        "-o",
        type=_base.Path(writable=True),
        help="Path of the output dir or file.",
    )
