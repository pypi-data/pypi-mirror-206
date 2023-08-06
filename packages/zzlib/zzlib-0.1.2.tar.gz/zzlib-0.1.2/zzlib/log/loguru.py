from logging import Formatter
import sys
from textwrap import indent
import traceback
from typing import Dict, Iterable

from loguru import *

from .. import func as _f
from .common import nearestParent, setVisibility, addScheme, getScheme, visibility


def recFilter(record: Dict):
    mode = record["extra"].pop("mode", "normal")
    minlevel = record["extra"].pop("minlevel", None)
    if mode == "disabled":
        return False
    if mode == "lib":
        level = nearestParent({**visibility["lib"], **visibility["normal"]}, record["name"]) or 0
        if minlevel:
            level = max(int(minlevel), level)
    elif mode == "force":
        level = int(minlevel) if minlevel else 0
    else:
        level = nearestParent(visibility["normal"], record["name"]) or 0
        if minlevel:
            level = max(int(minlevel), level)
    if record["level"].no < level:
        return False
    else:
        return True


def getRichDateFormat(style="default"):
    if style == "days":
        return "[%Y-%m-%d %H:%M:%S]"
    else:
        return "[%H:%M:%S]"


def getDateFormat(style="default"):
    if style == "days":
        return "{time:YYYY-MM-DD HH:mm:ss}"
    else:
        return "{time:HH:mm:ss}"


def getFormatter(style="default", datestyle="default"):
    def recFormatter(record: Dict):
        scheme = record.get("extra", {}).get("scheme", None)
        if scheme:
            schemed = getScheme(scheme, record)
        else:
            schemed = "{message}"
        datefmt = getDateFormat(datestyle)
        if style == "default":
            formatstr = (
                "<green>%s</green> | <level>{level: <8}</level> | <cyan>{name}</cyan> - <level>%s</level>\n"
                % (datefmt, schemed)
            )
            nindent = len(datefmt) + len(record["name"]) + 10
        elif style == "simple":
            formatstr = "<green>%s</green> <level>{level: >8}: %s</level>\n" % (
                datefmt,
                schemed,
            )
            nindent = len(datefmt) + 4
        elif style == "detailed":
            formatstr = (
                "<green>%s</green> | <level>{level: <8}</level> | <cyan>{name}:{function}:{line}</cyan> - <level>%s</level>\n"
                % (datefmt, schemed)
            )
            nindent = len(datefmt) + 7
        elif style == "rich":
            formatstr = schemed
        else:
            formatstr = style
        exp: RecordException = record.get("exception", None)
        if not style == "rich" and exp:
            expstr = indent(
                "".join(traceback.format_exception(exp.type, exp.value, exp.traceback)),
                " " * nindent,
            )
            expstr = expstr.replace("<", "\<").replace(">", "\>")
            formatstr += expstr
        return formatstr

    return recFormatter


logger.remove()
handler_id = logger.add(sys.stderr, filter=recFilter, format=getFormatter(), level=0)
handler_set = False


def getName(logger):
    return logger._options[-1].get("name", None)


def getMode(logger):
    return logger._options[-1].get("mode", "normal")


def initLogging(
    style: Iterable[str] = ("rich", "default"),
    datestyle: str = "default",
    stderr=True,
    force=True,
    richkw={},
    loggerkw={},
):
    global handler_id, handler_set
    if handler_set and not force:
        return
    logger.remove(handler_id)
    for s in _f.to_iterable(style):
        if s == "rich":
            if _f.is_in_notebook():
                continue
            try:
                from rich.logging import Console, RichHandler

                handler = RichHandler(
                    console=Console(stderr=stderr), markup=True, rich_tracebacks=True, **richkw
                )
                handler.setFormatter(Formatter(None, getRichDateFormat(datestyle)))
            except ImportError:
                continue
        else:
            handler = sys.stderr if stderr else sys.stdout
        handler_id = logger.add(
            handler, format=getFormatter(s, datestyle), filter=recFilter, level=0, **loggerkw
        )
        handler_set = True
        return logger


def prepLogger(
    name: str = None,
    mode: str = "normal",
    style: Iterable[str] = ("rich", "default"),
    datestyle: str = "default",
    stderr=True,
    richkw={},
    loggerkw={},
):
    if mode == "lib":
        setVisibility(40, name.split(".")[0], mode="lib")
    elif mode == "normal":
        initLogging(
            style=style,
            datestyle=datestyle,
            stderr=stderr,
            richkw=richkw,
            loggerkw=loggerkw,
            force=False,
        )
    return logger.bind(name=name, mode=mode)
