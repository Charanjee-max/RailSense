from sqlalchemy.orm import Session

from app.core.logger import logger

from app.crud.train_stop import get_train_stops

from app.exceptions.custom_exceptions import (
    ResourceNotFoundException,
)


def get_train_stops_service(
    db: Session,
    train_number: str,
):
    logger.info(
        f"Fetching train stops for train: {train_number}"
    )

    train_stops = get_train_stops(
        db=db,
        train_number=train_number,
    )

    if not train_stops:
        logger.warning(
            f"No train stops found for train: {train_number}"
        )

        raise ResourceNotFoundException(
            f"No stops found for train '{train_number}'."
        )

    logger.info(
        f"Fetched {len(train_stops)} stop(s) for train: {train_number}"
    )

    return train_stops