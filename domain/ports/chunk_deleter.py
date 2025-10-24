from typing import Protocol

from domain.entities import Chunk


class ChunkDeleter(Protocol):
    def delete(self, chunk: Chunk) -> None: ...
