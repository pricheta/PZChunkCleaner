from datetime import datetime
from pathlib import Path

import pytest
from unittest.mock import MagicMock, patch

from adapters.chunk_deleter.windows11 import Windows11ChunkDeleter
from domain.entities import Chunk

NOW = datetime.now()


@pytest.fixture
def mock_session():
    session = MagicMock()
    query = session.query.return_value
    filtered = query.filter.return_value
    filtered.delete.return_value = 1
    return session


@pytest.fixture
def tmp_dir(tmp_path):
    save_dir = tmp_path / "map"
    save_dir.mkdir()
    return tmp_path


@pytest.fixture()
def deleter(tmp_dir, mock_session):
    return Windows11ChunkDeleter(
        directory=tmp_dir,
        vehicle_db_session=mock_session,
    )


def test_delete_removes_file_and_db_record(deleter, tmp_dir, mock_session):
    chunk = Chunk(x_coordinate=10, y_coordinate=20, last_time_used_at=NOW)
    file_path = tmp_dir / "map" / "map_10_20.bin"
    file_path.write_text("test content")

    deleter.delete(chunk)

    assert not file_path.exists()

    mock_session.query.assert_called_once()
    mock_session.query.return_value.filter.assert_called_once()
    mock_session.query.return_value.filter.return_value.delete.assert_called_once_with(
        synchronize_session=False
    )
    mock_session.commit.assert_called_once()


def test_delete_raises_if_file_missing(deleter, tmp_dir, mock_session):
    chunk = Chunk(x_coordinate=10, y_coordinate=20, last_time_used_at=NOW)

    with pytest.raises(FileNotFoundError):
        deleter.delete(chunk)

    mock_session.commit.assert_not_called()


def test_custom_filename_template(tmp_dir, mock_session):
    deleter = Windows11ChunkDeleter(
        directory=tmp_dir,
        vehicle_db_session=mock_session,
        save_files_dir_name="map",
        filename_template="custom_{}_{}.dat",
    )

    chunk = Chunk(x_coordinate=10, y_coordinate=20, last_time_used_at=NOW)
    file_path = tmp_dir / "map" / "custom_10_20.dat"
    file_path.write_text("data")

    deleter.delete(chunk)

    assert not file_path.exists()
    mock_session.commit.assert_called_once()
