from datetime import datetime
from pathlib import Path

from domain.entities import Chunk
from domain.ports.chunk_fetcher import ChunkFetcher


class Windows11ChunkFetcher(ChunkFetcher):
    def __init__(
        self,
        directory: Path,
        save_files_dir_name: str = "map",
    ) -> None:
        self.directory = directory
        self.save_files_dir_name = save_files_dir_name

    def fetch(self) -> list[Chunk]:
        chunks = []

        for file in (self.directory / self.save_files_dir_name).iterdir():
            name = str(file.name).removesuffix(".bin")
            parts = name.split("_")

            x = int(parts[1])
            y = int(parts[2])

            stat = file.stat()
            last_used = datetime.fromtimestamp(stat.st_atime or stat.st_mtime)

            chunks.append(Chunk(x_coordinate=x, y_coordinate=y, created_at=last_used))

        return chunks
