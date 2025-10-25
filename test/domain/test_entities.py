from datetime import datetime

import pytest

from domain.entities import Chunk, ChunkArea


NOW = datetime.now()


def test_chunk_eq():
    first_chunk = Chunk(x_coordinate=1, y_coordinate=1, last_time_used_at=NOW)
    second_chunk = Chunk(x_coordinate=1, y_coordinate=1, last_time_used_at=NOW)
    assert first_chunk == second_chunk

    first_chunk = Chunk(x_coordinate=1, y_coordinate=1, last_time_used_at=NOW)
    second_chunk = Chunk(x_coordinate=1, y_coordinate=2, last_time_used_at=NOW)
    assert first_chunk != second_chunk

    first_chunk = Chunk(x_coordinate=1, y_coordinate=1, last_time_used_at=NOW)
    second_chunk = Chunk(x_coordinate=2, y_coordinate=1, last_time_used_at=NOW)
    assert first_chunk != second_chunk

    first_chunk = Chunk(x_coordinate=1, y_coordinate=1, last_time_used_at=NOW)
    second_chunk = Chunk(x_coordinate=2, y_coordinate=2, last_time_used_at=NOW)
    assert first_chunk != second_chunk

    first_chunk = "some_random_item"
    second_chunk = Chunk(x_coordinate=2, y_coordinate=2, last_time_used_at=NOW)
    assert first_chunk != second_chunk


def test_chunk_area_contains():
    chunk_area = ChunkArea(
        x_coordinate_start=1,
        y_coordinate_start=1,
        x_coordinate_end=2,
        y_coordinate_end=2,
    )

    for chunk in [
        Chunk(x_coordinate=1, y_coordinate=1, last_time_used_at=NOW),
        Chunk(x_coordinate=1, y_coordinate=2, last_time_used_at=NOW),
        Chunk(x_coordinate=2, y_coordinate=1, last_time_used_at=NOW),
        Chunk(x_coordinate=2, y_coordinate=2, last_time_used_at=NOW),
    ]:
        assert chunk in chunk_area

    for chunk in [
        "some_random_item",
        Chunk(x_coordinate=3, y_coordinate=1, last_time_used_at=NOW),
        Chunk(x_coordinate=1, y_coordinate=3, last_time_used_at=NOW),
    ]:
        assert not chunk in chunk_area


def test_chunk_area_validate():
    ChunkArea(
        x_coordinate_start=1,
        y_coordinate_start=1,
        x_coordinate_end=1,
        y_coordinate_end=1,
    )
    ChunkArea(
        x_coordinate_start=1,
        y_coordinate_start=1,
        x_coordinate_end=2,
        y_coordinate_end=2,
    )

    with pytest.raises(ValueError):
        ChunkArea(
            x_coordinate_start=2,
            y_coordinate_start=1,
            x_coordinate_end=1,
            y_coordinate_end=1,
        )

    with pytest.raises(ValueError):
        ChunkArea(
            x_coordinate_start=1,
            y_coordinate_start=2,
            x_coordinate_end=1,
            y_coordinate_end=1,
        )
