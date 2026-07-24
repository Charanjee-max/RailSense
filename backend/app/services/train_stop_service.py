from sqlalchemy.orm import Session

from app.crud.train_stop import get_train_stops

from app.exceptions.custom_exceptions import (
    ResourceNotFoundException,
)


def get_train_stops_service(
    db: Session,
    train_number: str,
):
    train_stops = get_train_stops(
        db=db,
        train_number=train_number,
    )

    if not train_stops:
        raise ResourceNotFoundException(
            f"No stops found for train '{train_number}'."
        )

    return train_stops