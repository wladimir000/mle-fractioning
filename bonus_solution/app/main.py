"""Minimal FastAPI CRUD app backed by Postgres."""

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import House
from .schemas import HouseCreate, HouseRead, HouseUpdate


app = FastAPI(
    title="Bonus Solution API",
    description="Reference FastAPI CRUD app for the optional project stretch goal.",
    version="1.0.0",
)
# Create the table automatically so the example can run without a separate
# migration step.
Base.metadata.create_all(bind=engine)


def _get_house_or_404(session: Session, house_id: int) -> House:
    """Return a house by ID or raise a consistent 404 response."""
    # Use one helper so every endpoint returns the same 404 message.
    house = session.query(House).filter(House.id == house_id).first()
    if house is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"House {house_id} was not found.",
        )
    return house


@app.get("/houses", response_model=list[HouseRead])
def list_houses(session: Session = Depends(get_db)) -> list[House]:
    """Return all stored houses ordered by ID."""
    # Returning rows in ID order makes the output predictable when testing or
    # checking the API in the docs UI.
    return session.query(House).order_by(House.id).all()


@app.post("/houses", response_model=HouseRead, status_code=status.HTTP_201_CREATED)
def create_house(payload: HouseCreate, session: Session = Depends(get_db)) -> House:
    """Create a new house record."""
    # Convert the validated request body into keyword arguments for the ORM
    # model, then save the new row.
    house = House(**payload.model_dump())
    session.add(house)
    session.commit()
    # Refresh the object so the response includes the generated primary key.
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

    # Update each model attribute from the validated request body.
    for field, value in payload.model_dump().items():
        setattr(house, field, value)

    session.commit()
    # Refresh before returning so the response matches the stored row.
    session.refresh(house)
    return house


@app.delete("/houses/{house_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_house(house_id: int, session: Session = Depends(get_db)) -> Response:
    """Delete a stored house record."""
    house = _get_house_or_404(session, house_id)
    session.delete(house)
    session.commit()
    # A 204 response means the delete succeeded and there is no response body.
    return Response(status_code=status.HTTP_204_NO_CONTENT)
