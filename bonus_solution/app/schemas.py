"""Pydantic schemas for the FastAPI bonus solution."""

from pydantic import BaseModel, ConfigDict, Field


class HouseBase(BaseModel):
    # Keep the shared field validation in one place so create, update, and read
    # schemas all use the same shape and constraints.
    bedrooms: int = Field(ge=0, le=20)
    bathrooms: float = Field(ge=0, le=20)
    sqft_living: int = Field(ge=100)
    grade: int = Field(ge=1, le=13)
    zipcode: str = Field(min_length=5, max_length=10)


class HouseCreate(HouseBase):
    """Request payload for creating a house."""


class HouseUpdate(HouseBase):
    # This example uses a full replacement update, so it has the same required
    # fields as the create payload.
    """Request payload for replacing a house."""


class HouseRead(HouseBase):
    """Response payload for house resources."""

    # Allow FastAPI to return SQLAlchemy model instances directly.
    model_config = ConfigDict(from_attributes=True)

    id: int
