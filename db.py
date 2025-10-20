from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer


Base = declarative_base()

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)
    wx = Column(Integer)
    wy = Column(Integer)


def get_session(db_path: Path):
    engine_str = 'sqlite:///' + str(db_path)
    engine = create_engine(engine_str, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()
