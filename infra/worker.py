import math
from datetime import datetime
from time import sleep
from typing import Callable

datetime_format = "%Y-%m-%dT%H-%M-%S"
get_now = lambda: datetime.now().strftime(datetime_format)


class Worker:
    def __init__(
        self,
        func: Callable,
        args = None,
        kwargs = None,
        immediate_run: bool = True,
        seconds_between_runs: int = 60,
        repeats: int | float = math.inf,
    ) -> None:
        self.func = func
        self.args = args or []
        self.kwargs = kwargs or {}
        self.immediate_run = immediate_run
        self.seconds_between_runs = seconds_between_runs
        self.repeats = repeats

    def run(self) -> None:
        if not self.immediate_run:
            sleep(self.seconds_between_runs)

        while self.repeats > 0:
            print(f'Calling {self.func.__name__} at {get_now()}')
            self.func(*self.args, **self.kwargs)
            sleep(self.seconds_between_runs)
            self.repeats -= 1
