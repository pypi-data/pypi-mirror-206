import asyncio
from functools import wraps
from typing import Callable, Union

from typer import Exit, Typer

from ...cls import Delayed


class AsyncTyper(Typer):
    """
    A typer that supports calling async commands.

    Args:
        on_interrupt: Function to be called when interruptted from async code.
        on_exception: Function to be called when uncaught exception raised from async code.
                      The exception will be passed as the first argument.
        hide_interrupt: Print '\r' when interruptted to remove '^C' printed by the console.
    """

    def __init__(
        self,
        *args,
        on_interrupt: Union[Callable, Delayed] = None,
        on_exception: Callable = None,
        hide_interrupt=True,
        **kw,
    ):
        super().__init__(*args, **kw)
        self.on_interrupt = Delayed(on_interrupt)
        self.on_exception = on_exception
        self.hide_interrupt = hide_interrupt

    def async_command(self, *args, **kwargs):
        def decorator(async_func):
            @wraps(async_func)
            def sync_func(*_args, **_kwargs):
                try:
                    return asyncio.run(async_func(*_args, **_kwargs))
                except KeyboardInterrupt:
                    if self.hide_interrupt:
                        print("\r", end="")
                    if self.on_interrupt:
                        self.on_interrupt.trigger()
                except Exception as e:
                    self.on_exception(e)
                    raise Exit(1) from None

            self.command(*args, **kwargs)(sync_func)
            return async_func

        return decorator
