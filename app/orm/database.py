"""Set database connection"""
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.settings import settings

SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = _session()
        yield db
    finally:
        db.close()
