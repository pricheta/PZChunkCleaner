from pathlib import Path

from pydantic import model_validator
from pydantic.v1 import BaseSettings


class ChunkCleanerConfig(BaseSettings):
    MAKE_BACKUP_FEATURE_FLAG: bool = True

    SAVE_FILE_DIR: Path = Path('C:/Users/pricheta/Zomboid/Saves/Sandbox/v5')

    SAVE_ZONE_FEATURE_FLAG: bool = True
    MAX_CHUNK_AGE_HOURS: int

    save_zone_x_coordinate_start: int | None = None
    save_zone_x_coordinate_end: int | None = None
    save_zone_y_coordinate_start: int | None = None
    save_zone_y_coordinate_end: int | None = None

    @model_validator(mode='after')
    def validate(self) -> None:
        if self.SAVE_ZONE_FEATURE_FLAG:
            if not all(
                [
                    self.save_zone_x_coordinate_start,
                    self.save_zone_x_coordinate_end,
                    self.save_zone_y_coordinate_start,
                    self.save_zone_y_coordinate_end,
                ]
            ):
                raise ValueError('If SAVE_ZONE_FEATURE_FLAG enabled all coordinates must be provided')
