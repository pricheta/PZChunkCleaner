from pathlib import Path

from pydantic.v1 import BaseSettings


class ChunkCleanerConfig(BaseSettings):
    MAKE_BACKUP_FEATURE_FLAG: bool = True
    MAX_CHUNK_AGE_MINUTES: int = 30
    SAVE_FILE_DIR: Path = Path("C:/Users/pricheta/Zomboid/Saves/Sandbox/test")
    IMMEDIATE_RUN: bool = True
    SECONDS_BETWEEN_RUNS: int = 60
    REPEATS: int | None = None
