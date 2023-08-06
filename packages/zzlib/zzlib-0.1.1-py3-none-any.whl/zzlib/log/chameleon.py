from __future__ import annotations

import inspect as _inspect
from typing import Callable
import warnings
from functools import cached_property
from logging import addLevelName

from .. import cls as _c
from .. import func as _f

TRACE = 5
addLevelName(TRACE, "TRACE")


class LoggerBase:
    def trace(self, msg, *args, **kw):
        raise NotImplementedError()

    def debug(self, msg, *args, **kw):
        raise NotImplementedError()

    def info(self, msg, *args, **kw):
        raise NotImplementedError()

    def warning(self, msg, *args, **kw):
        raise NotImplementedError()

    def error(self, msg, *args, **kw):
        raise NotImplementedError()

    def critical(self, msg, *args, **kw):
        raise NotImplementedError()

    def exception(self, msg, *args, **kw):
        raise NotImplementedError()

    def log(self, msg, *args, **kw):
        raise NotImplementedError()

    def opt(self, *args, **kw):
        raise NotImplementedError()

    def bind(self, **kw) -> LoggerBase:
        raise NotImplementedError()


class ChameleonLogger(_c.ProxyBase):
    __noproxy__ = ("module", "_kw", "__dict__")

    def __init__(self, by=("loguru", "logging"), **kw):
        for b in _f.to_iterable(by):
            try:
                if b == "loguru":
                    from . import loguru

                    self.module = loguru
                    break
                elif b == "logging":
                    from . import logging

                    self.module = logging
                    break
            except ImportError:
                pass
        else:
            warnings.warn(f'Logging is disabled due to lack of "{by}" lib.')
        self._kw = kw

    @cached_property
    def __subject__(self):
        return self.module.prepLogger(**self._kw)

    def setLevel(self, level=0, name=None, mode=None):
        m = self.module
        if name:
            mode = mode or self._kw.get("mode", "normal")
        else:
            name = m.getName(self)
            mode = m.getMode(self)
        return m.setVisibility(level, name, mode)

    def initLogging(self, *args, **kw):
        return self.module.initLogging(*args, **kw)

    def addScheme(self, *args, **kw):
        return self.module.addScheme(*args, **kw)


class LoggerCaller(LoggerBase):
    def __init__(self, **kw):
        self.kw = kw
        self._cache = {}

    def __getattribute__(self, attr):
        if attr in ("kw", "_cache", "configure"):
            return object.__getattribute__(self, attr)
        frame = _inspect.stack()[1]
        module = _inspect.getmodule(frame[0])
        name = module.__name__ if module else "__main__"
        if name in self._cache:
            logger = self._cache[name]
        else:
            logger = ChameleonLogger(name=name, **self.kw)
            self._cache[name] = logger
        return getattr(logger, attr)

    # Caller
    def configure(self, **kw):
        self.kw.update(kw)
        self._cache.clear()

    def __call__(self, **kw):
        kws = self.kw.copy()
        kws.update(kw)
        return LoggerCaller(**kws)

    # Chameleon
    @property
    def module(self):
        raise NotImplementedError()

    def setLevel(self, level=0, name=None, mode=None):
        raise NotImplementedError()

    def initLogging(self, style=("rich", "default"), datestyle="default", stderr=True):
        raise NotImplementedError()

    def addScheme(self, name: str, func: Callable):
        raise NotImplementedError()


logger = LoggerCaller()
liblogger = LoggerCaller(mode="lib")
forcelogger = LoggerCaller(mode="force")
