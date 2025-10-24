from pathlib import Path

from commands import make_directory_backup, MAKE_BACKUP_COMMAND
from db import get_session, Vehicle
from models import ChunkArea, Chunk


CHUNK_DATA_DIR = 'map'
VEHICLES_DB_NAME = 'vehicles.db'

MAKE_BACKUP_FEATURE_FLAG = True
CLEAR_CHUNKS_FEATURE_FLAG = True
CLEAR_CARS_FEATURE_FLAG = True


SAVE_CHUNK_AREA = ChunkArea.build_from_coordinates(
    first_x_coordinate=1034,
    first_y_coordinate=1472,
    second_x_coordinate=1045,
    second_y_coordinate=1480,
)



