import warnings
from typing import Union

from pandas import *

from .. import func as _f


def add_column_prefix(df: DataFrame, prefix: str):
    """Returns a DataFrame with column names prefixed"""
    _df = df.copy()
    _df.columns = prefix + "_" + _df.columns.values
    return _df


def show_table(
    df: Union[DataFrame, Series],
    index=True,
    index_col: str = "",
    digits=3,
    min_unwrap=3,
    by=("rich", "tabulate"),
    **kw,
):
    if isinstance(df, Series):
        df = df.to_frame()
    for b in _f.to_iterable(by):
        if b == "rich":
            try:
                from rich import box
                from rich.console import Console
                from rich.table import Table

                default = {"box": box.ROUNDED}
                default.update(kw)
                table = Table(**default)
                if index:
                    table.add_column(
                        index_col,
                        style="bold deep_sky_blue1",
                        justify="right",
                        no_wrap=True,
                    )
                for i, column in enumerate(df.columns):
                    no_wrap = i < min_unwrap or i > len(df.columns) - 1 - min_unwrap
                    table.add_column(str(column), header_style="bold", no_wrap=no_wrap)
                for i, value_list in enumerate(df.values.tolist()):
                    row = [str(i)] if index else []
                    for v in value_list:
                        if isinstance(v, float) and digits is not None:
                            v = "{val: .{digits}f}".format(val=v, digits=digits)
                        row.append(str(v))
                    table.add_row(*row)
                Console().print(table)
                break
            except ImportError:
                continue
        elif b == "tabulate":
            try:
                from tabulate import tabulate

                default = {"headers": "keys"}
                default.update(kw)
                print(tabulate(df, **default))
                break
            except ImportError:
                continue
    else:
        warnings.warn(f'Can not render table due to lack of "{by}" library, using print instead.')
        print(df)
