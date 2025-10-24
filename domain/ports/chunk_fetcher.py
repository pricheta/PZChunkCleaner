from typing import Protocol

from domain.entities import Chunk


class ChunkFetcher(Protocol):
    def fetch(self) -> list[Chunk]: ...
