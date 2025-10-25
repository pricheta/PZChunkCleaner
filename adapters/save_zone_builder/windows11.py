from domain.entities import ChunkArea
from domain.ports.save_zone_builder import SaveZoneBuilder


SAVE_ZONES = [
    ChunkArea(
        x_coordinate_start=1506,
        y_coordinate_start=890,
        x_coordinate_end=1512,
        y_coordinate_end=896,
    ),
]


class Windows11SaveZoneBuilder(SaveZoneBuilder):
    def build(self) -> list[ChunkArea]:
        return SAVE_ZONES
