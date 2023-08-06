from collections import namedtuple
import click
from typer.core import TyperCommand

OptionalValue = namedtuple("Flagged", ("noflag", "flag"))


class OptionalValueCommand(TyperCommand):
    def parse_args(self, ctx, args):
        long = {}
        short = {}
        defined = set()
        for o in self.params:
            if isinstance(o, click.Option):
                if isinstance(o.default, OptionalValue):
                    for pre in o.opts:
                        if pre.startswith("--"):
                            long[pre] = o
                        elif pre.startswith("-"):
                            short[pre] = o

        for i, a in enumerate(args):
            a = a.split("=")
            if a[0] in long:
                defined.add(long[a[0]])
                if len(a) == 1:
                    args[i] = f"{a[0]}={long[a[0]].default.flag}"
            elif a[0] in short:
                defined.add(short[a[0]])
                if len(args) == i + 1 or args[i + 1].startswith("-"):
                    args.insert(i + 1, str(short[a[0]].default.flag))

        for u in set(long.values()) - defined:
            for p, o in long.items():
                if o == u:
                    break
            args.append(f"{p}={u.default.noflag}")

        return super().parse_args(ctx, args)
