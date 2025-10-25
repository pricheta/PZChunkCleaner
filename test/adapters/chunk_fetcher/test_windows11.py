import os
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

import pytest

from adapters.chunk_fetcher.windows11 import Windows11ChunkFetcher
from domain.entities import Chunk

NOW = datetime.now()


@pytest.fixture
def tmp_dir(tmp_path):
    """Создаёт временную директорию с подпапкой map"""
    save_dir = tmp_path / "map"
    save_dir.mkdir()
    return tmp_path


def _create_fake_chunk_file(dir_path: Path, x: int, y: int, content: str = "data"):
    file_path = dir_path / f"map_{x}_{y}.bin"
    file_path.write_text(content)

    now_ts = NOW.timestamp()
    os.utime(file_path, (now_ts, now_ts))

    return file_path


def test_fetch_returns_correct_chunks(tmp_dir):
    map_dir = tmp_dir / "map"
    _create_fake_chunk_file(map_dir, 10, 20)
    _create_fake_chunk_file(map_dir, 5, 15)

    fetcher = Windows11ChunkFetcher(directory=tmp_dir)

    chunks = fetcher.fetch()

    assert len(chunks) == 2

    for chunk in chunks:
        assert isinstance(chunk, Chunk)
        assert isinstance(chunk.x_coordinate, int)
        assert isinstance(chunk.y_coordinate, int)
        assert isinstance(chunk.last_time_used_at, datetime)

    coords = sorted((c.x_coordinate, c.y_coordinate) for c in chunks)
    assert coords == [(5, 15), (10, 20)]


@patch("adapters.chunk_fetcher.windows11.datetime")
def test_fetch_uses_file_timestamps(mock_datetime, tmp_dir):
    map_dir = tmp_dir / "map"
    file_path = _create_fake_chunk_file(map_dir, 1, 2)

    fake_dt = datetime(2025, 10, 25, 13, 0, 0)
    mock_datetime.fromtimestamp.return_value = fake_dt

    fetcher = Windows11ChunkFetcher(directory=tmp_dir)
    chunks = fetcher.fetch()

    stat = file_path.stat()
    mock_datetime.fromtimestamp.assert_called_with(stat.st_atime or stat.st_mtime)

    assert chunks[0].last_time_used_at == fake_dt
