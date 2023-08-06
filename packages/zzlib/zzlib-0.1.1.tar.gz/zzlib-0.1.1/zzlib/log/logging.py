import sys
import logging
from logging import *
from logging import root
from typing import Any, Dict, Union

from .. import func as _f
from .common import nearestParent, setVisibility, addScheme, getScheme, visibility

if not root.hasHandlers():
    root.setLevel(DEBUG)

TRACE = 5
addLevelName(TRACE, "TRACE")


class LoggerAdapter(logging.LoggerAdapter):
    def __init__(
        self,
        logger: Union[logging.LoggerAdapter, Logger],
        kw: Dict[str, Any] = {},
        extra: Dict[str, Any] = {},
    ):
        if isinstance(logger, logging.LoggerAdapter):
            self.logger = logger.logger
            self.kw = {**logger.kw, **kw}
            self.extra = {**logger.extra, **extra}
        else:
            self.logger = logger
            self.kw = kw
            self.extra = extra

    def process(self, message: str, kw: Dict[str, Any]):
        kw.update(self.kw)
        if "extra" in kw:
            kw["extra"] = {**self.extra, **kw["extra"]}
        else:
            kw["extra"] = self.extra
        return message, kw

    def bind(self, **extra):
        return LoggerAdapter(self, extra=extra)

    def opt(self, exception=None, **okw):
        kw = {}
        if exception:
            kw["exc_info"] = exception
        return LoggerAdapter(self, kw=kw)

    def trace(self, message: str, *args, **kws):
        if self.isEnabledFor(TRACE):
            self._log(TRACE, message, args, **kws)


class CallableFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, defaults=None):
        if callable(fmt):
            self.fmtfunc = fmt
            fmt = None
        else:
            self.fmtfunc = None
        if callable(datefmt):
            self.datefmtfunc = fmt
            datefmt = None
        else:
            self.datefmtfunc = None
        super().__init__(fmt, datefmt, style="{")

    def format(self, record):
        fmt = self.fmtfunc(record) if self.fmtfunc else None
        datefmt = self.datefmtfunc(record) if self.datefmtfunc else None
        if fmt or datefmt:
            super().__init__(fmt or self._fmt, datefmt or self.datefmt, style="{")

        return super().format(record)


def recFilter(record):
    mode = record.__dict__.pop("mode", "normal")
    minlevel = record.__dict__.pop("minlevel", None)
    if mode == "disabled":
        return False
    elif mode == "lib":
        level = nearestParent({**visibility["lib"], **visibility["normal"]}, record.name) or 0
        if minlevel:
            level = max(int(minlevel), level)
    elif mode == "force":
        level = int(minlevel) if minlevel else 0
    else:
        level = nearestParent(visibility["normal"], record.name) or 0
        if minlevel:
            level = max(int(minlevel), level)
    if record.levelno < level:
        return False
    else:
        return True


def getDateFormat(style="default"):
    if style == "days":
        return "%Y-%m-%d %H:%M:%S"
    else:
        return "%H:%M:%S"


def getFormatter(style="default", datestyle="default"):
    def recFormatter(record: LogRecord):
        scheme = getattr(record, "scheme", None)
        if scheme:
            schemed = getScheme(scheme, record)
        else:
            schemed = "{message}"
        if style == "default":
            return "{asctime} | {levelname: <8} | {name} - %s" % schemed
        elif style == "simple":
            return "{asctime} {levelname}: %s" % schemed
        elif style == "detailed":
            return "{asctime} | {levelname: <8} | {name}:{funcName}:{lineno} - %s" % schemed
        elif style == "rich":
            return schemed
        else:
            return style

    if style == "rich":
        datefmt = f"[{getDateFormat(datestyle)}]"
    else:
        datefmt = getDateFormat(datestyle)
    return CallableFormatter(recFormatter, datefmt)


def getName(logger: LoggerAdapter):
    return logger.name


def getMode(logger: LoggerAdapter):
    return logger.extra.get("mode", "normal")


def getHandler(style=("rich", "default"), datestyle="default", stderr=True):
    for s in _f.to_iterable(style):
        if s == "rich":
            if _f.is_in_notebook():
                continue
            try:
                from rich.logging import Console, RichHandler

                handler = RichHandler(console=Console(stderr=stderr))
                break
            except ImportError:
                continue
        else:
            handler = StreamHandler(sys.stderr if stderr else sys.stdout)
            break
    handler.setFormatter(getFormatter(s, datestyle))
    return handler


def setIsolated(logger: LoggerAdapter, force=False, **kw):
    if logger.hasHandlers() and force:
        logger.handlers.clear()
    if not logger.hasHandlers():
        handler = getHandler(**kw)
        handler.addFilter(recFilter)
        logger.addHandler(handler)
    logger.propagate = False


def initLogging(force=True, level=10, **kw):
    if root.hasHandlers():
        if not force:
            return
        for handler in root.handlers:
            if hasattr(handler, "_zzlib_added"):
                root.removeHandler(handler)
    handler = getHandler(**kw)
    handler._zzlib_added = True
    handler.addFilter(recFilter)
    root.addHandler(handler)
    root.setLevel(level)


def prepLogger(name: str = None, mode="normal", **kw):
    logger = getLogger(name)
    if mode == "lib":
        setVisibility(40, name.split(".")[0], mode="lib")
    elif mode == "force":
        setIsolated(logger, **kw)
    else:
        initLogging(force=False, **kw)
    return LoggerAdapter(logger, extra={"mode": mode})
