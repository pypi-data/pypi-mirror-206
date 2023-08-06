import re
from logging import LogRecord
from typing import Callable

visibility = {"normal": {}, "lib": {}}
schemes = {}


def nearestParent(d: dict, name: str):
    split = name.split(".")
    for i in range(-1, len(split)):
        parent = ".".join(split[:-i])
        if parent in d:
            return d[parent]


def setVisibility(level, name: str, force=True, mode=None):
    if not mode:
        mode = "normal"
    if mode == "lib":
        if force or level < nearestParent(visibility["lib"], name) or 0:
            visibility[mode][name] = level
    elif mode != "force":
        if force or level > nearestParent(visibility[mode], name) or 0:
            visibility[mode][name] = level


def addScheme(name, scheme: str):
    schemes[name] = scheme


def reprSchemeVar(record, var):
    extra = re.match(r"extra\[(\w*)\]", var)
    if isinstance(record, LogRecord):
        if extra:
            var = extra.group(1)
        if var in record.__dict__:
            return "{%s}" % var
    elif isinstance(record, dict):
        if extra:
            if extra.group(1) in record.get("extra", {}):
                return "{%s}" % var
        else:
            if var in record:
                return "{%s}" % var
    return ""


def getScheme(name, record):
    if not schemes.get(name, None):
        raise ValueError(f"scheme {name} not found")
    else:
        scheme = schemes[name]
    repr_pattern = r"{([\[\]\w]+)}"
    for optional in re.findall(r"<([^<]+)>", scheme):
        vars = list(re.finditer(repr_pattern, optional))
        if not vars:
            continue
        else:
            exists = all(reprSchemeVar(record, var.group(1)) for var in vars)
        scheme = scheme.replace(f"<{optional}>", optional if exists else "")
    for var in re.findall(repr_pattern, scheme):
        scheme = scheme.replace("{%s}" % var, reprSchemeVar(record, var))
    return scheme
