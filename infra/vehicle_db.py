from functools import lru_cache
from pathlib import Path

from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

db_filename = "vehicles.db"


class Base(DeclarativeBase):
    pass


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)
    wx = Column(Integer)
    wy = Column(Integer)


@lru_cache(maxsize=1)
def get_vehicle_db_session(directory: Path):
    engine_str = "sqlite:///" + str(directory / db_filename)
    engine = create_engine(engine_str, echo=False)
    Session = sessionmaker(bind=engine)
    return Session()
