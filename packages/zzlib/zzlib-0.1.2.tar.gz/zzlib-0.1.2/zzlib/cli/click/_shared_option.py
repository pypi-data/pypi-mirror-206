from functools import partial, partialmethod
import types

from click import Argument, Command, Context, Group, MultiCommand, command, group
from click.core import ParameterSource


class GroupWithSharedOptions(Group):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.shared_cmd = None
        self.shared_params = {}

    def shared(self):
        def deco(func):
            self.shared_cmd = cmd = command(func)
            for p in cmd.params:
                if isinstance(p, Argument):
                    raise TypeError("arguments can not be shared")
            self.params.extend(cmd.params)
            return cmd

        return deco

    def invoke(self, ctx):
        avail = self._avail_shared_params(ctx)
        for cmd in self.commands.values():
            if not isinstance(cmd, MultiCommand):
                cmd.invoke = types.MethodType(self._cmd_invoke, cmd)
            for c in avail:
                for p in cmd.params:
                    if set(c.opts) & set(p.opts):
                        break
                else:
                    cmd.params.append(c)
        self._backward(ctx)
        for c in avail:
            ctx.params.pop(c.name)
        Group.invoke(self, ctx)

    def group(self, *args, **kw):
        if "cls" not in kw:
            kw["cls"] = type(self)
        return super().group(*args, **kw)

    def _params_of(self, cmd: Command):
        return [p.name for p in cmd.params]

    def _backward(self, ctx: Context, params=None):
        cmd = ctx.command
        if params is None:
            params = {
                k: v for k, v in ctx.params.items() if ctx.get_parameter_source(k) != ParameterSource.DEFAULT
            }
        if isinstance(cmd, MultiCommand) and getattr(cmd, "shared_cmd", None):
            avail_params = self._params_of(cmd.shared_cmd)
            parsed = []
            for p, v in params.items():
                if p in avail_params:
                    cmd.shared_params[p] = v
                    parsed.append(p)
            params = {k: v for k, v in params.items() if k not in parsed}
        if ctx.parent:
            self._backward(ctx.parent, params=params)

    def _backinvoke(self, ctx: Context):
        cmd = ctx.command
        if isinstance(cmd, MultiCommand) and getattr(cmd, "shared_cmd", None):
            sub_ctx = ctx._make_sub_context(cmd.shared_cmd)
            sub_ctx.params = cmd.shared_params
            for p in cmd.shared_cmd.params:
                if not p.name in sub_ctx.params:
                    sub_ctx.params[p.name] = p.get_default(ctx)
            cmd.shared_cmd.invoke(sub_ctx)
        if ctx.parent:
            self._backinvoke(ctx.parent)

    def _avail_shared_params(self, ctx: Context):
        avail = set()
        if ctx is None:
            return avail
        cmd = ctx.command
        if getattr(cmd, "shared_cmd", None):
            avail = set(cmd.shared_cmd.params)
        return avail | self._avail_shared_params(ctx.parent)

    def _cmd_invoke(self, cmd: Command, ctx: Context):
        self._backward(ctx)
        self._backinvoke(ctx)
        for p in self._avail_shared_params(ctx):
            ctx.params.pop(p.name, None)
        Command.invoke(cmd, ctx)


sogroup = partial(group, cls=GroupWithSharedOptions)
Group.sogroup = partialmethod(Group.group, cls=GroupWithSharedOptions)
