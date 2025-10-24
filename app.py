from adapters.backuper.windows11 import Windows11Backuper
from adapters.chunk_deleter.windows11 import Windows11ChunkDeleter
from adapters.chunk_fetcher.windows11 import Windows11ChunkFetcher
from adapters.save_zone_builder.windows11 import Windows11SaveZoneBuilder
from domain.core.chunk_cleaner import ChunkCleaner
from domain.core.config import ChunkCleanerConfig
from infra.vehicle_db import get_vehicle_db_session
from infra.worker import Worker


if __name__ == "__main__":
    chunk_cleaner_config = ChunkCleanerConfig()
    vehicle_db_session = get_vehicle_db_session(
        directory=chunk_cleaner_config.SAVE_FILE_DIR,
    )

    backuper = Windows11Backuper(
        directory=chunk_cleaner_config.SAVE_FILE_DIR,
    )
    chunk_fetcher = Windows11ChunkFetcher(
        directory=chunk_cleaner_config.SAVE_FILE_DIR,
    )
    save_zone_builder = Windows11SaveZoneBuilder()
    chunk_deleter = Windows11ChunkDeleter(
        directory=chunk_cleaner_config.SAVE_FILE_DIR,
        vehicle_db_session=vehicle_db_session,
    )
    chunk_cleaner = ChunkCleaner(
        config=chunk_cleaner_config,
        backuper=backuper,
        chunk_fetcher=chunk_fetcher,
        save_zone_builder=save_zone_builder,
        chunk_deleter=chunk_deleter,
    )

    app = Worker(
        func=chunk_cleaner.clean,
        immediate_run=chunk_cleaner_config.IMMEDIATE_RUN,
        seconds_between_runs=chunk_cleaner_config.SECONDS_BETWEEN_RUNS,
        repeats=chunk_cleaner_config.REPEATS,
    )
    app.run()
