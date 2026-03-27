"""Pydantic schemas for the FastAPI bonus solution.

These schemas define the public API contract for request validation and
response serialization.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class HouseBase(BaseModel):
    """Shared house fields used by create and update requests.

    The field constraints keep the example small while still showing how input
    validation can live close to the API boundary.
    """

    bedrooms: int = Field(ge=0, le=20)
    bathrooms: float = Field(ge=0, le=20)
    sqft_living: int = Field(ge=100)
    grade: int = Field(ge=1, le=13)
    zipcode: str = Field(min_length=5, max_length=10)


class HouseCreate(HouseBase):
    """Request payload for creating a house."""


class HouseUpdate(HouseBase):
    """Request payload for replacing a house."""


class HouseRead(HouseBase):
    """Response payload for house resources."""

    # Allow FastAPI to serialize directly from SQLAlchemy model instances.
    model_config = ConfigDict(from_attributes=True)

    id: int
