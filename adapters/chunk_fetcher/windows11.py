import os
from datetime import datetime
from pathlib import Path

from domain.entities import Chunk
from domain.ports.chunk_fetcher import ChunkFetcher


class Windows11ChunkFetcher(ChunkFetcher):
    def __init__(
        self,
    ) -> None:
        ...

    def fetch(self) -> list[Chunk]:
        ...
