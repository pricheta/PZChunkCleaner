from datetime import datetime
from typing import Any

from pydantic import BaseModel






    @classmethod
    def build_from_filename(cls, filename: str):
        name = filename.removesuffix(".bin")
        parts = name.split("_")

        x = int(parts[1])
        y = int(parts[2])

        return Chunk(x_coordinate=x, y_coordinate=y)


