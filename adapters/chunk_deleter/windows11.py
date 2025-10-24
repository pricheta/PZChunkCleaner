from pathlib import Path

from sqlalchemy import and_
from sqlalchemy.orm import Session

from domain.entities import Chunk
from domain.ports.chunk_deleter import ChunkDeleter
from infra.vehicle_db import Vehicle


class Windows11ChunkDeleter(ChunkDeleter):
    def __init__(
        self,
        directory: Path,
        vehicle_db_session: Session,
        filename_template: str = "map_{}_{}.bin",
    ) -> None:
        self.directory = directory
        self.vehicle_db_session = vehicle_db_session
        self.filename_template = filename_template

    def delete(self, chunk: Chunk) -> None:
        filename = self.filename_template.format(chunk.x_coordinate, chunk.y_coordinate)
        (self.directory / filename).unlink()

        self.vehicle_db_session.query(Vehicle).filter(
            and_(Vehicle.wx == chunk.x_coordinate, Vehicle.wy == chunk.y_coordinate)
        ).delete(synchronize_session=False)
        self.vehicle_db_session.commit()
