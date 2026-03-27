"""SQLAlchemy models for the FastAPI bonus solution.

The ORM layer maps Python objects to the Postgres tables used by the bonus app.
"""

from __future__ import annotations

from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class House(Base):
    """Persisted house record for the reference CRUD API.

    The model mirrors the five fields requested in the stretch goal so the API
    stays easy to compare against the project brief.
    """

    __tablename__ = "houses"

    # The example stays intentionally small: one surrogate key plus the five
    # fields called out in the project brief.
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bedrooms: Mapped[int] = mapped_column(Integer, nullable=False)
    bathrooms: Mapped[float] = mapped_column(Float, nullable=False)
    sqft_living: Mapped[int] = mapped_column(Integer, nullable=False)
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    zipcode: Mapped[str] = mapped_column(String(10), nullable=False)
