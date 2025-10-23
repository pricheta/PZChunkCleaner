from typing import Any

from pydantic import BaseModel


class Chunk(BaseModel):
    x_coordinate: int
    y_coordinate: int

    def __eq__(self, other: Any):
        if not isinstance(other, Chunk):
            return False
        return self.x_coordinate == other.x_coordinate and self.y_coordinate == other.y_coordinate

    @classmethod
    def build_from_filename(cls, filename: str):
        name = filename.removesuffix(".bin")
        parts = name.split("_")

        x = int(parts[1])
        y = int(parts[2])

        return Chunk(x_coordinate=x, y_coordinate=y)

class ChunkArea(BaseModel):
    chunks: list[Chunk]

    def __contains__(self, item: Any):
        return item in self.chunks

    @classmethod
    def build_from_coordinates(
        cls,
        first_x_coordinate: int,
        first_y_coordinate: int,
        second_x_coordinate: int,
        second_y_coordinate: int,
    ):
        start_x_coordinate = min(first_x_coordinate, second_x_coordinate)
        end_x_coordinate = max(first_x_coordinate, second_x_coordinate)

        start_y_coordinate = min(first_y_coordinate, second_y_coordinate)
        end_y_coordinate = max(first_y_coordinate, second_y_coordinate)

        chunks = []
        for x in range(start_x_coordinate, end_x_coordinate + 1):
            for y in range(start_y_coordinate, end_y_coordinate + 1):
                chunks.append(Chunk(x_coordinate=x, y_coordinate=y))

        return cls(chunks=chunks)

