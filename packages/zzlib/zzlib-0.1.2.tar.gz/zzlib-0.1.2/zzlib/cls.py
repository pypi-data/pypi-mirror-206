import inspect
from types import FunctionType
from typing import Callable


class _DefaultType:
    def __new__(cls):
        return Def

    def __reduce__(self):
        return (_DefaultType, ())

    def __bool__(self):
        return False


Def = object.__new__(_DefaultType)


class Delayed:
    def __init__(self, func: Callable):
        if isinstance(func, Delayed):
            self.func = func.func
            self.args = func.args
            self.kw = func.kw
        else:
            self.func = func
            self.args = ()
            self.kw = {}

    def __call__(self, *args, **kw):
        self.args = args
        self.kw = kw
        return self

    def trigger(self, **kw):
        if self:
            return self.func(*self.args, **{**self.kw, **kw})

    def __bool__(self):
        return bool(self.func)

    def __repr__(self):
        return f"<{self.__class__.__name__} definition for {self.func.__name__} at {hex(id(self))}>"


class Singleton(type):
    """A metaclass to create a singleton."""

    _instances = {}

    def __call__(cls, *args, **kw):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kw)
        return cls._instances[cls]


class PatcherMeta(type):
    """A transparent proxy metaclass that run __upgrade__ for patching existing classes without changing its fingerprint."""

    def __call__(cls, *args, **kw):
        chain = [cls]
        while type(chain[-1]) == type(cls):
            chain.append(chain[-1].__base__)
        if len(args) == 1 and not kw and isinstance(args[0], chain[-1]):
            if not isinstance(args[0], cls.__base__):
                obj = cls.__base__(args[0])
            else:
                obj = args[0]
            obj.__class__ = cls
        else:
            obj = super(type(cls), cls).__call__(*args, **kw)
        for p in reversed(chain[:-1]):
            try:
                p.__upgrade__(obj)
            except AttributeError:
                continue
        return obj


class Patcher(metaclass=PatcherMeta):
    pass


class ProxyBase:
    """
    A proxy class that make accesses just like direct access to __subject__ if not overwriten in the class.
    Attributes defined in class. attrs named in __noproxy__ will not be proxied to __subject__.
    """

    __slots__ = ()

    def __call__(self, *args, **kw):
        return self.__subject__(*args, **kw)

    def hasattr(self, attr):
        try:
            object.__getattribute__(self, attr)
            return True
        except AttributeError:
            return False

    def __getattribute__(self, attr, oga=object.__getattribute__):
        if attr.startswith("__") and attr not in oga(self, "_noproxy"):
            subject = oga(self, "__subject__")
            if attr == "__subject__":
                return subject
            return getattr(subject, attr)
        return oga(self, attr)

    def __getattr__(self, attr, oga=object.__getattribute__):
        if attr == "hasattr" or self.hasattr(attr):
            return oga(self, attr)
        else:
            return getattr(oga(self, "__subject__"), attr)

    @property
    def _noproxy(self, oga=object.__getattribute__):
        base = oga(self, "__class__")
        for cls in inspect.getmro(base):
            if hasattr(cls, "__noproxy__"):
                yield from cls.__noproxy__

    def __setattr__(self, attr, val, osa=object.__setattr__):
        if attr == "__subject__" or attr in self._noproxy:
            return osa(self, attr, val)
        return setattr(self.__subject__, attr, val)

    def __delattr__(self, attr, oda=object.__delattr__):
        if attr == "__subject__" or hasattr(type(self), attr) and not attr.startswith("__"):
            oda(self, attr)
        else:
            delattr(self.__subject__, attr)

    def __instancecheck__(self, cls):
        if cls in (Proxy, ProxyBase):
            return True
        return isinstance(self.__subject__, cls)

    def __bool__(self):
        return bool(self.__subject__)

    def __getitem__(self, arg):
        return self.__subject__[arg]

    def __setitem__(self, arg, val):
        self.__subject__[arg] = val

    def __delitem__(self, arg):
        del self.__subject__[arg]

    def __getslice__(self, i, j):
        return self.__subject__[i:j]

    def __setslice__(self, i, j, val):
        self.__subject__[i:j] = val

    def __delslice__(self, i, j):
        del self.__subject__[i:j]

    def __contains__(self, ob):
        return ob in self.__subject__

    for name in "repr str hash len abs complex int long float iter".split():
        exec("def __%s__(self): return %s(self.__subject__)" % (name, name))

    for name in "cmp", "coerce", "divmod":
        exec("def __%s__(self, ob): return %s(self.__subject__, ob)" % (name, name))

    for name, op in [
        ("lt", "<"),
        ("gt", ">"),
        ("le", "<="),
        ("ge", ">="),
        ("eq", " == "),
        ("ne", "!="),
    ]:
        exec("def __%s__(self, ob): return self.__subject__ %s ob" % (name, op))

    for name, op in [("neg", "-"), ("pos", "+"), ("invert", "~")]:
        exec("def __%s__(self): return %s self.__subject__" % (name, op))

    for name, op in [
        ("or", "|"),
        ("and", "&"),
        ("xor", "^"),
        ("lshift", "<<"),
        ("rshift", ">>"),
        ("add", "+"),
        ("sub", "-"),
        ("mul", "*"),
        ("div", "/"),
        ("mod", "%"),
        ("truediv", "/"),
        ("floordiv", "//"),
    ]:
        exec(
            (
                "def __%(name)s__(self, ob):\n"
                "    return self.__subject__ %(op)s ob\n"
                "\n"
                "def __r%(name)s__(self, ob):\n"
                "    return ob %(op)s self.__subject__\n"
                "\n"
                "def __i%(name)s__(self, ob):\n"
                "    self.__subject__ %(op)s=ob\n"
                "    return self\n"
            )
            % locals()
        )

    del name, op

    def __index__(self):
        return self.__subject__.__index__()

    def __rdivmod__(self, ob):
        return divmod(ob, self.__subject__)

    def __pow__(self, *args):
        return pow(self.__subject__, *args)

    def __ipow__(self, ob):
        self.__subject__ **= ob
        return self

    def __rpow__(self, ob):
        return pow(ob, self.__subject__)


class Proxy(ProxyBase):
    def __init__(self, val):
        self.set(val)

    def set(self, val):
        self.__subject__ = val


class FactoryProxy(Delayed, ProxyBase):
    __noproxy__ = ("func", "args", "kw")

    @property
    def __subject__(self):
        return super().trigger()


class LazyLoad(FactoryProxy):
    """A class to initialize when calling load."""

    __noproxy__ = ("_val",)

    @property
    def is_loaded(self):
        return self.hasattr("_val")

    def load(self, force=False):
        if force or not self.is_loaded:
            self._val = self.trigger()
        return self._val

    @property
    def __subject__(self):
        try:
            return object.__getattribute__(self, "_val")
        except AttributeError:
            raise AttributeError("this lazy object has not been loaded") from None


class DecoMeta(type):
    def __init__(cls, name: str, bases: tuple, attrs: dict):
        deco = getattr(cls, "__deco__", None)
        if isinstance(deco, FunctionType):
            for fname, func in attrs.items():
                if isinstance(func, FunctionType):
                    setattr(cls, fname, deco(func))
