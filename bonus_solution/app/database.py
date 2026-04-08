"""Database configuration for the FastAPI bonus solution."""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


def _default_database_url() -> str:
    """Build the default Postgres connection string from environment variables."""
    # These defaults match the service names and credentials in docker-compose,
    # so the app can connect without extra local setup.
    return (
        "postgresql+psycopg://"
        f"{os.getenv('POSTGRES_USER', 'postgres')}:"
        f"{os.getenv('POSTGRES_PASSWORD', 'postgres')}@"
        f"{os.getenv('POSTGRES_HOST', 'db')}:"
        f"{os.getenv('POSTGRES_PORT', '5432')}/"
        f"{os.getenv('POSTGRES_DB', 'houses')}"
    )


DATABASE_URL = os.getenv("DATABASE_URL", _default_database_url())

# Keep the SQLAlchemy setup in one place so the route handlers stay focused on
# request and response logic.
engine = create_engine(DATABASE_URL)
# Disable autocommit so each route controls when its changes are saved.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# All ORM models inherit from this shared base class.
Base = declarative_base()


def get_db():
    """Yield one SQLAlchemy session per request and close it afterward."""
    # FastAPI treats this generator as a dependency and injects one session
    # into each request handler that asks for it.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
