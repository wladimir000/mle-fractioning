"""Minimal FastAPI CRUD app backed by Postgres.

This module wires together the FastAPI routes, SQLAlchemy session dependency,
and the small CRUD flow used by the reference stretch-goal solution.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import House
from .schemas import HouseCreate, HouseRead, HouseUpdate


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """Create database tables when the application starts."""
    # For a teaching example, eager table creation keeps the stack runnable
    # without adding a separate migration tool.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Bonus Solution API",
    description="Reference FastAPI CRUD app for the optional project stretch goal.",
    version="1.0.0",
    lifespan=lifespan,
)


def _get_house_or_404(session: Session, house_id: int) -> House:
    """Return a house by ID or raise a consistent 404 response."""
    # Centralize the not-found check so every endpoint returns the same error.
    house = session.get(House, house_id)
    if house is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"House {house_id} was not found.",
        )
    return house


@app.get("/houses", response_model=list[HouseRead])
def list_houses(session: Session = Depends(get_db)) -> list[House]:
    """Return all stored houses ordered by ID."""
    # Ordering by ID keeps the example deterministic for demos and tests.
    statement = select(House).order_by(House.id)
    return list(session.scalars(statement))


@app.post("/houses", response_model=HouseRead, status_code=status.HTTP_201_CREATED)
def create_house(payload: HouseCreate, session: Session = Depends(get_db)) -> House:
    """Create a new house record."""
    # `model_dump()` converts the validated Pydantic payload into plain values
    # that can be passed straight into the ORM model.
    house = House(**payload.model_dump())
    session.add(house)
    session.commit()
    # Refresh so the generated primary key is included in the response body.
    session.refresh(house)
    return house


@app.get("/houses/{house_id}", response_model=HouseRead)
def get_house(house_id: int, session: Session = Depends(get_db)) -> House:
    """Fetch a single house by ID."""
    return _get_house_or_404(session, house_id)


@app.put("/houses/{house_id}", response_model=HouseRead)
def update_house(
    house_id: int,
    payload: HouseUpdate,
    session: Session = Depends(get_db),
) -> House:
    """Replace a stored house record."""
    house = _get_house_or_404(session, house_id)

    # Apply a full replacement update to keep the endpoint behavior simple.
    for field, value in payload.model_dump().items():
        setattr(house, field, value)

    session.add(house)
    session.commit()
    # Refresh after commit so the returned object matches the stored state.
    session.refresh(house)
    return house


@app.delete("/houses/{house_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_house(house_id: int, session: Session = Depends(get_db)) -> Response:
    """Delete a stored house record."""
    house = _get_house_or_404(session, house_id)
    session.delete(house)
    session.commit()
    # Return an explicit empty 204 response to match common REST semantics.
    return Response(status_code=status.HTTP_204_NO_CONTENT)
