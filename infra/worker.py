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
        immediate_run: bool,
        seconds_between_runs: int,
        args=None,
        kwargs=None,
        repeats: int | float = math.inf,
    ) -> None:
        self.func = func
        self.immediate_run = immediate_run
        self.seconds_between_runs = seconds_between_runs
        self.args = args or []
        self.kwargs = kwargs or {}
        self.repeats = repeats

    def run(self) -> None:
        if not self.immediate_run:
            sleep(self.seconds_between_runs)

        while True:
            print(f"Calling {self.func.__name__} at {get_now()}")
            self.func(*self.args, **self.kwargs)

            self.repeats -= 1
            if self.repeats <= 0:
                break

            sleep(self.seconds_between_runs)
