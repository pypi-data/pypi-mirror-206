import re
import shutil
import textwrap
import time
from collections import namedtuple
from contextlib import closing
from datetime import datetime, timedelta
from enum import Enum
from functools import cached_property
from queue import Queue
from threading import Event, Lock, Thread, current_thread
from typing import Callable, Iterable, Sized, Union

from . import cls as _c
from . import func as _f
from . import mixin as _m


class Merged(_m.ThreadingMixin):
    def __init__(self, *its, endswhen="all"):
        super().__init__()
        self.iterators = its
        self.endswhen = endswhen

    @staticmethod
    def _produce(it, q: Queue):
        try:
            with closing(it) as cit:
                for i in cit:
                    q.put(i)
        except _m.SentinelStop:
            pass
        finally:
            q.put(_m.SentinelStop)

    def _session(self, queue):
        for it in self.iterators:
            t = Thread(target=self._produce, args=(it, queue))
            t.daemon = True
            t.start()
            yield t

    def __iter__(self):
        queue = Queue()
        n_ends = 0
        with self.session(queue):
            while True:
                out = queue.get()
                if out is _m.SentinelStop:
                    if self.endswhen in ("first", "any"):
                        break
                    elif self.endswhen == "all":
                        n_ends += 1
                        if n_ends == len(self.iterators):
                            break
                    continue
                yield out


class IterQueue(Queue):
    def __iter__(self):
        yield from self._history()

    def follow(self, history=True):
        if history:
            yield from self._history_follow()
        else:
            yield from self._follow()

    def _history(self):
        with self.mutex:
            batch = list(self.queue)
        yield from batch

    def _history_follow(self):
        with self.mutex:
            batch = list(self.queue)
            size = len(batch)
        yield from batch
        yield from self._follow(size=size)

    def _follow(self, size=None):
        size = size or self.qsize()
        while True:
            with self.mutex:
                sizep = len(self.queue)
                batch = []
                for i in range(size, sizep):
                    batch.append(self.queue[i])
            yield from batch
            size = sizep
            time.sleep(0.1)


class Timer(_m.StopableMixin):
    def __init__(self, timeout: Union[timedelta, int, float] = None, start=True):
        super().__init__()
        self._begin = None
        self._extra = timedelta(0)
        if isinstance(timeout, timedelta):
            self.timeout = timeout.seconds
        else:
            self.timeout = timeout
        if start:
            self.start()

    def start(self, reset=False):
        if reset:
            self._extra = timedelta(0)
        self._begin = datetime.now()
        self._stop_event.clear()

    def pause(self):
        if not self.is_paused():
            self._extra = self.elapsed
            self._begin = None

    def watch(self, on_timeout=None, on_stop=None):
        def _daemon():
            while not self.is_stopped():
                if self.is_timeout():
                    return self._trigger_callback(on_timeout)
                self._sleep_interval()
            else:
                return self._trigger_callback(on_stop)

        if not self._begin:
            raise ValueError("this timer has not been started yet")
        if self.is_stopped():
            raise ValueError("this timer is stopped")
        t = Thread(target=_daemon)
        t.daemon = True
        t.start()
        return t

    def wait(self):
        if not self._begin:
            raise ValueError("this timer has not been started yet")
        while not self.is_stopped():
            if self.is_timeout():
                break
            self._sleep_interval()
        else:
            return False
        return True

    @property
    def elapsed(self):
        if not self._begin:
            return self._extra
        else:
            return datetime.now() - self._begin + self._extra

    def is_paused(self):
        return self._begin is None

    def is_timeout(self):
        if not self.timeout:
            return False
        return self.elapsed > timedelta(seconds=float(self.timeout))

    def is_ticking(self):
        return (not self.is_stopped()) and (not self.is_timeout())

    def _sleep_interval(self, fraction=0.01):
        if self.timeout:
            time.sleep(min(10, max(0.1, self.timeout * fraction)))
        else:
            time.sleep(0.1)

    @staticmethod
    def _trigger_callback(callback: Union[str, Exception, Callable, _c.Delayed] = None):
        if isinstance(callback, str):
            raise TimeoutError(callback)
        if isinstance(callback, Exception):
            raise callback
        if callable(callback):
            return _c.Delayed(callback).trigger()
        return None

    def __repr__(self):
        if self.is_stopped():
            spec = "stopped"
        elif self.is_timeout():
            spec = "timeout"
        else:
            spec = "ticking"
        return f"<{self.__class__.__name__} ({spec}) at {hex(id(self))}>"


class Timeout(Timer):
    def during(self, it: Iterable):
        def _waiter():
            self.wait()
            return
            yield

        return Merged(it, _waiter(), endswhen="first")

    def __iter__(self):
        while True:
            yield self.elapsed
            if self.is_timeout():
                break

    def __enter__(self):
        self.watch(on_timeout=_c.Delayed(_f.async_raise)(current_thread().ident, TimeoutError))
        return self

    def __exit__(self, type, value, traceback):
        self.stop()


class TimedCache(_c.FactoryProxy):
    __noproxy__ = ("_val", "timer", "lock", "onupdate")

    def __init__(self, func: Callable, timeout=None, onupdate: Callable = None):
        super().__init__(func)
        self.timer = Timer(timeout, start=False)
        self.onupdate = onupdate
        self.lock = Lock()

    def freeze(self):
        self.timer.stop()

    def update(self):
        self._val = val = self.trigger()
        self.timer.start()
        return val

    def noupdate(self):
        with self.lock:
            return object.__getattribute__(self, "_val")

    def updated(self, forceupdate=False, noupdate=False):
        if forceupdate and noupdate:
            raise ValueError("can not use forceupdate and noupdate simultaneously")
        if forceupdate:
            val = self.update()
            self._on_update()
            return val
        if noupdate:
            return self.noupdate()
        else:
            return self.__subject__

    def _on_update(self):
        if self.onupdate:
            _c.Delayed(self.onupdate).trigger()

    @property
    def __subject__(self):
        updated = False
        with _f.nonblocking(self.lock) as locked:
            if locked and (
                (not self.hasattr("_val")) or (self.timer.is_timeout() and not self.timer.is_stopped())
            ):
                self.update()
                updated = True
        if updated:
            self._on_update()
        return self.noupdate()


class LoggerPattern:
    def __init__(self):
        self._patterns = []

    def add(
        self,
        func: Callable,
        match=r".*",
        format: str = None,
        processors: Iterable[Callable] = (),
    ):
        self._patterns.append((func, match, format, processors))
        return self

    def ignore(self, match):
        self._patterns.insert(0, (None, match, None, ()))
        return self

    @staticmethod
    def width_limit_processor(width=None):
        if not width:
            width = shutil.get_terminal_size((140, 140)).columns - 70

        def p(line: str):
            lines = textwrap.wrap(line, width) if width else [line]
            yield from lines

        return p

    def render(self, item):
        if isinstance(item, Sized) and len(item) == 2 and not isinstance(item, str):
            line, pattern = item
            line = str(line)
            if isinstance(item, Sized):
                if len(pattern) == 1:
                    func = pattern
                    processors = None
                else:
                    func, processors = pattern
        else:
            line = str(item)
            for func, match, format, processors in self._patterns:
                if match:
                    matches = re.match(match, line, re.IGNORECASE)
                    if matches:
                        groups = matches.groups()
                        if format is None:
                            line = ", ".join(*groups) if groups else matches.group(0)
                        else:
                            line = format.format(*groups)
                        break
                else:
                    break
        if func:
            for line in self._apply_processors(processors=processors, lines=[line]):
                func(line)

    def _apply_processors(self, processors: Iterable[Callable], lines: Iterable[str]):
        if processors:
            p, *ops = processors
            for l in lines:
                if ops:
                    yield from self._apply_processors(ops, p(l))
                else:
                    yield from p(l)
        else:
            yield from lines


class Logger(_m.ThreadingMixin):
    lock = Lock()

    def __init__(self):
        super().__init__()
        self.sources = {}

    def add(self, source: Iterable[str], pattern: LoggerPattern):
        self.sources[source] = pattern
        return self

    def start(self, wait=False):
        if wait:
            with self.session():
                self.join()
        else:
            super().start()

    def _session(self):
        for s, p in self.sources.items():
            t = Thread(target=self._daemon, args=[s, p])
            t.daemon = True
            t.start()
            yield t

    def _daemon(self, source: Iterable, pattern: LoggerPattern):
        try:
            for s in source:
                with self.lock:
                    pattern.render(s)
        except _m.SentinelStop:
            pass


EventTiming = Enum("EventTiming", "CONTINUOUS ON_BEING ON_NOT_BEING")
InitialState = Enum("InitialState", "NONE FIRST ERROR")
EventCondition = namedtuple(
    "EventCondition",
    ["event", "condition", "timing"],
    defaults=(True, EventTiming.ON_BEING),
)


class EventSource(_c.Delayed):
    def __init__(
        self,
        func: Callable,
        conditions: Iterable[EventCondition] = (),
        initial=InitialState.NONE,
    ):
        super().__init__(func)
        self.value = initial
        self.conditions = list(conditions)
        self._lock = Lock()

    def add(self, event, condition=True, timing=EventTiming.ON_BEING):
        if isinstance(timing, str):
            timing = EventTiming[timing.upper()]
        self.conditions.append(EventCondition(event, condition, timing))
        return self

    @property
    def value(self):
        return self._last_val

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            try:
                val = InitialState[val.upper()]
            except KeyError:
                pass
        self._last_val = val

    def check(self, queue):
        t = Thread(target=self._check, args=(queue,))
        t.daemon = True
        t.start()

    def _check(self, queue):
        with _f.nonblocking(self._lock) as locked:
            if locked:
                try:
                    val = self.trigger()
                except Exception:
                    val = InitialState.ERROR
                for c in self.conditions:
                    current_match = self._check_condition(val, c.condition)
                    # print(f'{self.func.__name__} Match: {current_match} ({val})')
                    if c.timing == EventTiming.CONTINUOUS:
                        if current_match == True:
                            queue.put(c.event)
                    else:
                        last_match = self._check_condition(self._last_val, c.condition)
                        # print(f'{self.func.__name__} Last Match: {last_match} ({self._last_val})')
                        if c.timing == EventTiming.ON_BEING and current_match == True and not last_match:
                            queue.put(c.event)
                        elif (
                            c.timing == EventTiming.ON_NOT_BEING and last_match == True and not current_match
                        ):
                            queue.put(c.event)
                self._last_val = val

    @staticmethod
    def _check_condition(val, condition):
        if val == InitialState.ERROR:
            return False
        if val == InitialState.FIRST:
            return object()
        if val == InitialState.NONE:
            return None
        if callable(condition):
            try:
                return bool(condition(val))
            except:
                return False
        else:
            return type(condition)(val) == condition


class BinaryEventSource(EventSource):
    def __init__(self, func: Callable, whenTrue=None, whenFalse=None, initial=InitialState.NONE):
        cs = []
        if whenTrue is not None:
            cs.append(EventCondition(whenTrue, True, EventTiming.ON_BEING))
        if whenFalse is not None:
            cs.append(EventCondition(whenFalse, False, EventTiming.ON_BEING))
        super().__init__(func, cs, initial=initial)


class CallbackQueue(IterQueue):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.callbacks = []

    def put(self, item, **kw):
        for i in _f.pipeline([item], *self.callbacks):
            super().put(i, **kw)


class Eventer(_m.ThreadingMixin):
    def __init__(self, *sources: EventSource, interval: float = 1.0):
        super().__init__()
        self.sources = list(sources)
        self.interval = interval
        self._events = CallbackQueue()
        self._lock = Lock()

    def put(self, *args, **kw):
        self._events.put(*args, **kw)

    def get(self, *args, **kw):
        self._events.get(*args, **kw)

    def check(self):
        for s in self.sources:
            s.check(self._events)

    def check_loop(self):
        try:
            while True:
                self.check()
                time.sleep(float(self.interval))
        except _m.SentinelStop:
            pass

    def _session(self):
        t = Thread(target=self.check_loop)
        t.daemon = True
        t.start()
        yield t

    def add_processor(self, processor):
        if not callable(processor):
            raise TypeError("processor must be callable")
        self._events.callbacks.insert(0, processor)

    def add_callback(self, callback, events=None):
        if not callable(callback):
            raise TypeError("callback must be callable")

        def processor(es):
            for e in es:
                if events is None or e in _f.to_iterable(events):
                    ret = callback(e)
                else:
                    ret = None
                yield e
                if isinstance(ret, Iterable):
                    yield from ret
                elif ret is not None:
                    yield ret

        self.add_processor(processor)

    def event_flag(self, events, flag=None):
        if not isinstance(flag, Event):
            flag = Event()

        def setter(e):
            flag.set()

        self.add_callback(setter, events=events)
        return flag

    def wait(self, events, history=True, timeout=None):
        for e in Timeout(timeout).during(self.events(history=history)):
            if e in _f.to_iterable(events):
                return True
        else:
            return False

    def events(self, history=True):
        with self.shared_session():
            yield from self._events.follow(history)

    def __iter__(self):
        yield from self._events


class Checker(_c.FactoryProxy):
    __noproxy__ = ("options", "__dict__")

    def __init__(self, func: Callable, **kw):
        super().__init__(func)
        self.options = kw

    def when(self, val):
        self.options["when"] = val
        return self

    def on(self, val):
        if isinstance(val, str):
            val = EventTiming[val.upper()]
        self.options["on"] = val
        return self

    def event(self, val):
        self.options["event"] = val
        return self

    def wait(self, timeout=None):
        self.options.setdefault("event", object())
        return self.__subject__.wait(self.options["event"], timeout=timeout)

    @cached_property
    def __subject__(self):
        return self._get_eventer(self, **self.options)

    @staticmethod
    def _get_eventer(
        delayed,
        event,
        when=True,
        on=EventTiming.ON_BEING,
        initial=InitialState.NONE,
        interval=1.0,
    ):
        condition = EventCondition(event, when, on)
        source = EventSource(delayed, [condition], initial=initial)
        return Eventer(source, interval=interval)
