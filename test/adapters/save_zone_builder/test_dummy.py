from domain.entities import ChunkArea
from adapters.save_zone_builder.dummy import (
    DummySaveZoneBuilder,
    SAVE_ZONES,
)


def test_build_returns_predefined_save_zones():
    builder = DummySaveZoneBuilder()
    zones = builder.build()

    assert zones == SAVE_ZONES


def test_build_returns_same_reference_data():
    builder = DummySaveZoneBuilder()

    first_call = builder.build()
    second_call = builder.build()

    assert first_call is second_call
    assert first_call[0] is SAVE_ZONES[0]
