from typing import Protocol


class Backuper(Protocol):
    def run(self) -> None: ...
