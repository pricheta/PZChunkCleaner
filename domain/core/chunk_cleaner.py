from datetime import datetime, timedelta

from domain.core.config import ChunkCleanerConfig
from domain.entities import Chunk
from domain.ports.backuper import Backuper
from domain.ports.chunk_deleter import ChunkDeleter
from domain.ports.chunk_fetcher import ChunkFetcher
from domain.ports.save_zone_builder import SaveZoneBuilder


class ChunkCleaner:
    def __init__(
        self,
        config: ChunkCleanerConfig,
        backuper: Backuper,
        chunk_fetcher: ChunkFetcher,
        save_zone_builder: SaveZoneBuilder,
        chunk_deleter: ChunkDeleter,
    ):
        self.config = config
        self.backuper = backuper
        self.chunk_fetcher = chunk_fetcher
        self.save_zone_builder = save_zone_builder
        self.chunk_deleter = chunk_deleter

    def clean(self):
        if self.config.MAKE_BACKUP_FEATURE_FLAG:
            self.backuper.run()

        chunks = self.chunk_fetcher.fetch()
        save_zones = self.save_zone_builder.build()
        threshold_datetime = datetime.now() - timedelta(hours=self.config.MAX_CHUNK_AGE_HOURS)

        for chunk in chunks:
            if any((chunk in save_zone for save_zone in save_zones)):
                continue
            if chunk.created_at <= threshold_datetime:
                continue
            self.chunk_deleter.delete(chunk)













if __name__ == '__main__':
    if MAKE_BACKUP_FEATURE_FLAG:
        make_directory_backup(SAVE_DIRS_PATH / SAVE_DIR_NAME)

    if CLEAR_CHUNKS_FEATURE_FLAG:
        for file in (SAVE_DIRS_PATH / SAVE_DIR_NAME / CHUNK_DATA_DIR).iterdir():
            chunk = Chunk.build_from_filename(str(file.name))

            if chunk not in SAVE_CHUNK_AREA:
                (SAVE_DIRS_PATH / SAVE_DIR_NAME / CHUNK_DATA_DIR / file).unlink()

    if CLEAR_CARS_FEATURE_FLAG:
        try:
            session = get_session(SAVE_DIRS_PATH / SAVE_DIR_NAME / VEHICLES_DB_NAME)
            vehicles = session.query(Vehicle).all()

            for vehicle in vehicles:
                chunk = Chunk(x_coordinate=vehicle.wx, y_coordinate=vehicle.wy)

                if chunk not in SAVE_CHUNK_AREA:
                    session.delete(vehicle)
            session.commit()
        except:
            print('Возникла ошибка при очистке автомобилей')