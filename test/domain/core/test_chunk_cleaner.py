from datetime import datetime, timedelta
from unittest.mock import Mock

import pytest

from domain.core.chunk_cleaner import ChunkCleaner
from domain.core.config import ChunkCleanerConfig
from domain.entities import Chunk, ChunkArea
from domain.ports.backuper import Backuper
from domain.ports.chunk_deleter import ChunkDeleter
from domain.ports.chunk_fetcher import ChunkFetcher
from domain.ports.save_zone_builder import SaveZoneBuilder


NOW = datetime.now()


@pytest.fixture()
def config():
    return ChunkCleanerConfig()


@pytest.fixture()
def backuper() -> Backuper:
    return Mock(spec=Backuper)


@pytest.fixture()
def chunk_fetcher() -> ChunkFetcher:
    chunk_fetcher = Mock(spec=ChunkFetcher)
    chunk_fetcher.fetch.return_value = [
        Chunk(x_coordinate=1, y_coordinate=1, last_time_used_at=NOW),
        Chunk(x_coordinate=1, y_coordinate=3, last_time_used_at=NOW),
        Chunk(x_coordinate=1, y_coordinate=4, last_time_used_at=NOW - timedelta(hours=1)),
    ]
    return chunk_fetcher


@pytest.fixture()
def save_zone_builder() -> SaveZoneBuilder:
    save_zone_builder = Mock(spec=SaveZoneBuilder)
    save_zone_builder.build.return_value = [
        ChunkArea(
            x_coordinate_start=1,
            y_coordinate_start=1,
            x_coordinate_end=1,
            y_coordinate_end=2,
        ),
    ]
    return save_zone_builder


@pytest.fixture()
def chunk_deleter() -> ChunkDeleter:
    return Mock(spec=ChunkDeleter)


@pytest.fixture()
def chunk_cleaner(
    config,
    backuper,
    chunk_fetcher,
    save_zone_builder,
    chunk_deleter,
):
    return ChunkCleaner(
        config=config,
        backuper=backuper,
        chunk_fetcher=chunk_fetcher,
        save_zone_builder=save_zone_builder,
        chunk_deleter=chunk_deleter,
    )


def test_clean_success(config, chunk_cleaner):
    config.MAKE_BACKUP_FEATURE_FLAG = True
    config.MAX_CHUNK_AGE_MINUTES = 1

    chunk_cleaner.clean()

    chunk_cleaner.backuper.run.assert_called_once()
    chunk_cleaner.chunk_fetcher.fetch.assert_called_once()
    chunk_cleaner.save_zone_builder.build.assert_called_once()

    chunk_cleaner.chunk_deleter.delete.assert_called_once_with(
        Chunk(x_coordinate=1, y_coordinate=4, last_time_used_at=NOW - timedelta(hours=1))
    )


def test_clean_success_no_backup(config, chunk_cleaner):
    config.MAKE_BACKUP_FEATURE_FLAG = False
    chunk_cleaner.clean()

    chunk_cleaner.backuper.run.assert_not_called()
