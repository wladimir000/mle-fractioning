"""SQLAlchemy models for the FastAPI bonus solution."""

from sqlalchemy import Column, Float, Integer, String

from .database import Base


class House(Base):
    # Map this model to the `houses` table in Postgres.
    __tablename__ = "houses"

    # The columns below mirror the five fields required in the stretch goal,
    # plus an integer primary key used to identify each row.
    id = Column(Integer, primary_key=True, index=True)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Float, nullable=False)
    sqft_living = Column(Integer, nullable=False)
    grade = Column(Integer, nullable=False)
    zipcode = Column(String(10), nullable=False)
