"""Database configuration for the FastAPI bonus solution.

This module keeps the SQLAlchemy setup in one place so the rest of the app can
focus on request handling and data modeling.
"""

from __future__ import annotations

import os
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


def _default_database_url() -> str:
    """Build the default Postgres connection string from environment variables."""
    # Keep local Docker development simple by deriving the URL from the
    # same env vars used by docker-compose.
    return (
        "postgresql+psycopg://"
        f"{os.getenv('POSTGRES_USER', 'postgres')}:"
        f"{os.getenv('POSTGRES_PASSWORD', 'postgres')}@"
        f"{os.getenv('POSTGRES_HOST', 'db')}:"
        f"{os.getenv('POSTGRES_PORT', '5432')}/"
        f"{os.getenv('POSTGRES_DB', 'houses')}"
    )


DATABASE_URL = os.getenv("DATABASE_URL", _default_database_url())


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""


engine = create_engine(DATABASE_URL, future=True)
# Use one short-lived session per request so handlers can commit independently
# without sharing state across requests.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db() -> Generator[Session, None, None]:
    """Yield one SQLAlchemy session per request and close it afterward."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
