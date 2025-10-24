from pathlib import Path

from pydantic.v1 import BaseSettings


class ChunkCleanerConfig(BaseSettings):
    MAKE_BACKUP_FEATURE_FLAG: bool = True
    MAX_CHUNK_AGE_HOURS: int

    SAVE_FILE_DIR: Path = Path('C:/Users/pricheta/Zomboid/Saves/Sandbox/v5')
