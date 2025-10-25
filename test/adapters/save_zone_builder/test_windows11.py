from domain.entities import ChunkArea
from adapters.save_zone_builder.windows11 import (
    Windows11SaveZoneBuilder,
    SAVE_ZONES,
)


def test_build_returns_predefined_save_zones():
    builder = Windows11SaveZoneBuilder()
    zones = builder.build()

    assert zones == SAVE_ZONES


def test_build_returns_same_reference_data():
    builder = Windows11SaveZoneBuilder()

    first_call = builder.build()
    second_call = builder.build()

    assert first_call is second_call
    assert first_call[0] is SAVE_ZONES[0]
