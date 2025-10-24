from functools import lru_cache
from pathlib import Path

from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)
    wx = Column(Integer)
    wy = Column(Integer)


@lru_cache(maxsize=1)
def get_vehicle_db_session(db_path: Path):
    engine_str = 'sqlite:///' + str(db_path)
    engine = create_engine(engine_str, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()
