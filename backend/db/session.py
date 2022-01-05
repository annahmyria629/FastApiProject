from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# We are creating a sqlalchemy engine with postgres database URL.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Once we create an instance of the SessionLocal class, this instance will be the actual database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
