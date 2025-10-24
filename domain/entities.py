from datetime import datetime
from typing import Any, Self

from pydantic import BaseModel, model_validator


class Chunk(BaseModel):
    x_coordinate: int
    y_coordinate: int
    created_at: datetime | None = None

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Chunk):
            return False
        return self.x_coordinate == other.x_coordinate and self.y_coordinate == other.y_coordinate


class ChunkArea(BaseModel):
    x_coordinate_start: int
    y_coordinate_start: int
    x_coordinate_end: int
    y_coordinate_end: int

    def __contains__(self, chunk: Any) -> bool:
        if not isinstance(chunk, Chunk):
            return False

        return (
            self.x_coordinate_start <= chunk.x_coordinate <= self.x_coordinate_end and
            self.y_coordinate_start <= chunk.y_coordinate <= self.y_coordinate_end
        )

    @model_validator(mode='after')
    def validate_coordinates(self) -> Self:
        if self.x_coordinate_start > self.x_coordinate_end:
            raise ValueError('x start coordinate must be greater or equal to x end coordinate')
        if self.y_coordinate_start > self.y_coordinate_end:
            raise ValueError('y start coordinate must be greater or equal to y end coordinate')
        return self