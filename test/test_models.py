from typing import Callable

from models import Chunk, ChunkArea

def print_logs(func: Callable):
    def wrapper(*args, **kwargs):
        print('---------------')
        print('Запуск теста ' + func.__name__)
        func(*args, **kwargs)
        print('Успешно!')

    return wrapper


@print_logs
def test_chunk_eq():
    first_chunk = Chunk(x_coordinate=1, y_coordinate=1)
    second_chunk = Chunk(x_coordinate=1, y_coordinate=1)
    assert first_chunk == second_chunk


    first_chunk = Chunk(x_coordinate=1, y_coordinate=1)
    second_chunk = Chunk(x_coordinate=1, y_coordinate=2)
    assert first_chunk != second_chunk

    first_chunk = Chunk(x_coordinate=1, y_coordinate=1)
    second_chunk = Chunk(x_coordinate=2, y_coordinate=1)
    assert first_chunk != second_chunk

    first_chunk = Chunk(x_coordinate=1, y_coordinate=1)
    second_chunk = Chunk(x_coordinate=2, y_coordinate=2)
    assert first_chunk != second_chunk

    first_chunk = Chunk(x_coordinate=1, y_coordinate=1)
    second_chunk = 5
    assert first_chunk != second_chunk


@print_logs
def test_chunk_build_from_filename():
    chunk = Chunk.build_from_filename('map_1_2.bin')
    assert chunk == Chunk(x_coordinate=1, y_coordinate=2)


@print_logs
def test_chunk_area_build_from_coordinates():
    area = ChunkArea.build_from_coordinates(
        1, 2, 1, 2
    )
    assert area.chunks == [
        Chunk(x_coordinate=1, y_coordinate=1),
        Chunk(x_coordinate=1, y_coordinate=2),
        Chunk(x_coordinate=2, y_coordinate=1),
        Chunk(x_coordinate=2, y_coordinate=2)
    ]

    area = ChunkArea.build_from_coordinates(
        2, 1, 2, 1
    )
    assert area.chunks == [
        Chunk(x_coordinate=1, y_coordinate=1),
        Chunk(x_coordinate=1, y_coordinate=2),
        Chunk(x_coordinate=2, y_coordinate=1),
        Chunk(x_coordinate=2, y_coordinate=2)
    ]


test_chunk_eq()
test_chunk_build_from_filename()
test_chunk_area_build_from_coordinates()