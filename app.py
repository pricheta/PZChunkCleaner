from pathlib import Path

from commands import make_directory_backup
from models import ChunkArea, Chunk

SAVE_DIRS_PATH = Path('C:/Users/pricheta/Zomboid/Saves/Sandbox')
SAVE_DIR_NAME = 'test'
CHUNK_DATA_DIR = 'map'


SAVE_CHUNK_AREA = ChunkArea.build_from_coordinates(
    1024,
    1055,
    1472,
    1503,
)


if __name__ == '__main__':
    make_directory_backup(SAVE_DIRS_PATH / SAVE_DIR_NAME)

    for file in (SAVE_DIRS_PATH / SAVE_DIR_NAME / CHUNK_DATA_DIR).iterdir():
        chunk = Chunk.build_from_filename(str(file.name))

        if chunk not in SAVE_CHUNK_AREA:
            (SAVE_DIRS_PATH / SAVE_DIR_NAME / CHUNK_DATA_DIR / file).unlink()
