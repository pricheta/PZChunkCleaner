from typing import Protocol

from domain.entities import ChunkArea


class SaveZoneBuilder(Protocol):
    def build(self) -> list[ChunkArea]: ...
