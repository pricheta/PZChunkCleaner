from pathlib import Path

from commands import make_directory_backup, MAKE_BACKUP_COMMAND
from db import get_session, Vehicle
from models import ChunkArea, Chunk

SAVE_DIRS_PATH = Path('C:/Users/pricheta/Zomboid/Saves/Sandbox')
SAVE_DIR_NAME = 'v3'

CHUNK_DATA_DIR = 'map'
VEHICLES_DB_NAME = 'vehicles.db'

MAKE_BACKUP_FEATURE_FLAG = True
CLEAR_CHUNKS_FEATURE_FLAG = True
CLEAR_CARS_FEATURE_FLAG = True


SAVE_CHUNK_AREA = ChunkArea.build_from_coordinates(
    1024,
    1055,
    1472,
    1503,
)


if __name__ == '__main__':
    if MAKE_BACKUP_FEATURE_FLAG:
        make_directory_backup(SAVE_DIRS_PATH / SAVE_DIR_NAME)

    if CLEAR_CHUNKS_FEATURE_FLAG:
        for file in (SAVE_DIRS_PATH / SAVE_DIR_NAME / CHUNK_DATA_DIR).iterdir():
            chunk = Chunk.build_from_filename(str(file.name))

            if chunk not in SAVE_CHUNK_AREA:
                (SAVE_DIRS_PATH / SAVE_DIR_NAME / CHUNK_DATA_DIR / file).unlink()

    if CLEAR_CARS_FEATURE_FLAG:
        session = get_session(SAVE_DIRS_PATH / SAVE_DIR_NAME / VEHICLES_DB_NAME)
        vehicles = session.query(Vehicle).all()

        for vehicle in vehicles:
            chunk = Chunk(x_coordinate=vehicle.wx, y_coordinate=vehicle.wy)

            if chunk not in SAVE_CHUNK_AREA:
                session.delete(vehicle)

        session.commit()

