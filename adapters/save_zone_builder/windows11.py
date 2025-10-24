from domain.entities import ChunkArea
from domain.ports.save_zone_builder import SaveZoneBuilder


SAVE_ZONES = [
    ChunkArea(
        x_coordinate_start=200,
        y_coordinate_start=200,
        x_coordinate_end=200,
        y_coordinate_end=200,
    ),
]


class Windows11SaveZoneBuilder(SaveZoneBuilder):
    def build(self) -> list[ChunkArea]:
        return SAVE_ZONES
