from pathlib import Path
from typing import Protocol


class Backuper(Protocol):
    def run(self, directory: Path) -> None:
        ...
