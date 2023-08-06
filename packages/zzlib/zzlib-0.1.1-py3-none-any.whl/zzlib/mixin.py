from contextlib import contextmanager
from threading import Event, Lock, Thread
from typing import Generator, Iterator

from . import func as _f


class StopableMixin:
    def __init__(self):
        self._stop_event = Event()

    def stop(self):
        self._stop_event.set()

    def is_stopped(self):
        return self._stop_event.is_set()


class SentinelStop(Exception):
    pass


class ThreadingMixin:
    shared_sid = object()

    def __init__(self):
        self._slaves = {}
        self._shared_count = 0
        self.mutex = Lock()

    def stop(self, sid=None):
        # print(f'Stopping session {sid} of {self.__class__.__name__}.')
        with self.mutex:
            if sid:
                if sid is self.shared_sid:
                    self._shared_count -= 1
                    if self._shared_count > 0:
                        return
                slaves = self._slaves.pop(sid, ())
            else:
                slaves = _f.flatten(list(self._slaves.values()))
            for t in slaves:
                if isinstance(t, Thread):
                    tid = _f.get_tid(t)
                    if tid:
                        _f.async_raise(tid, SentinelStop)
            if not sid:
                self._slaves.clear()

    def add_slave(self, sid, t):
        with self.mutex:
            if sid not in self._slaves:
                self._slaves[sid] = []
            self._slaves[sid].append(t)

    @contextmanager
    def session(self, *args, **kw):
        sid = self.start(*args, **kw)
        try:
            yield sid
        finally:
            self.stop(sid)

    def shared_session(self, *args, **kw):
        return self.session(*args, sid=self.shared_sid, **kw)

    def start(self, *args, sid=None, **kw):
        if not sid:
            sid = object()
        elif sid is self.shared_sid:
            with self.mutex:
                self._shared_count += 1
                if self._shared_count > 1:
                    return sid
        for s in self._session(*args, **kw):
            if s:
                self.add_slave(sid, s)
        return sid

    def join(self):
        for t in _f.flatten(list(self._slaves.values())):
            if isinstance(t, Thread):
                t.join()

    def _session(self):
        yield

    def __del__(self):
        self.stop()
