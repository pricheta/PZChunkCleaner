from datetime import datetime, timedelta

from domain.core.config import ChunkCleanerConfig
from domain.ports.backuper import Backuper
from domain.ports.chunk_deleter import ChunkDeleter
from domain.ports.chunk_fetcher import ChunkFetcher
from domain.ports.save_zone_builder import SaveZoneBuilder


class ChunkCleaner:
    def __init__(
        self,
        config: ChunkCleanerConfig,
        backuper: Backuper,
        chunk_fetcher: ChunkFetcher,
        save_zone_builder: SaveZoneBuilder,
        chunk_deleter: ChunkDeleter,
    ):
        self.config = config
        self.backuper = backuper
        self.chunk_fetcher = chunk_fetcher
        self.save_zone_builder = save_zone_builder
        self.chunk_deleter = chunk_deleter

    def clean(self):
        if self.config.MAKE_BACKUP_FEATURE_FLAG:
            self.backuper.run()

        chunks = self.chunk_fetcher.fetch()
        save_zones = self.save_zone_builder.build()
        threshold_datetime = datetime.now() - timedelta(
            hours=self.config.MAX_CHUNK_AGE_HOURS
        )

        for chunk in chunks:
            if any((chunk in save_zone for save_zone in save_zones)):
                continue
            if threshold_datetime <= chunk.created_at:
                continue
            self.chunk_deleter.delete(chunk)
