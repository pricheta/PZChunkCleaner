import os
from datetime import datetime
from pathlib import Path

from domain.entities import Chunk
from domain.ports.chunk_fetcher import ChunkFetcher


class Windows11ChunkFetcher(ChunkFetcher):
    def __init__(
        self,
        directory: Path,
    ) -> None:
        self.directory = directory

    def fetch(self) -> list[Chunk]:
        chunks = []

        for file in self.directory.iterdir():
            name = str(file.name).removesuffix(".bin")
            parts = name.split("_")

            x = int(parts[1])
            y = int(parts[2])

            chunks.append(Chunk(x_coordinate=x, y_coordinate=y))

        return chunks
