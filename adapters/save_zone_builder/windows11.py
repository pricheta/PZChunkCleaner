from domain.entities import ChunkArea
from domain.ports.save_zone_builder import SaveZoneBuilder


SAVE_ZONES = [
    ChunkArea(
        x_coordinate_start=1041,
        y_coordinate_start=1475,
        x_coordinate_end=1041,
        y_coordinate_end=1475,
    ),
]


class Windows11SaveZoneBuilder(SaveZoneBuilder):
    def build(self) -> list[ChunkArea]:
        return SAVE_ZONES
