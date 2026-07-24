from sqlalchemy.orm import Session

from app.core.logger import logger

from app.crud.train_running_days import (
    create_running_days,
    get_all_running_days,
    get_running_days_by_train,
)

from app.exceptions.custom_exceptions import (
    ResourceNotFoundException,
)


def create_running_days_service(
    db: Session,
    data,
):
    logger.info(
        f"Creating running days for train: {data.TrainNumber}"
    )

    running_days = create_running_days(
        db=db,
        data=data,
    )

    logger.info(
        f"Running days created successfully for train: {running_days.TrainNumber}"
    )

    return running_days


def get_all_running_days_service(
    db: Session,
):
    logger.info("Fetching all running days")

    running_days = get_all_running_days(
        db=db,
    )

    logger.info(
        f"Fetched {len(running_days)} running day record(s)"
    )

    return running_days


def get_running_days_by_train_service(
    db: Session,
    train_number: str,
):
    logger.info(
        f"Fetching running days for train: {train_number}"
    )

    running_days = get_running_days_by_train(
        db=db,
        train_number=train_number,
    )

    if not running_days:
        logger.warning(
            f"Running days not found for train: {train_number}"
        )

        raise ResourceNotFoundException(
            f"Running days not found for train '{train_number}'."
        )

    logger.info(
        f"Successfully fetched running days for train: {train_number}"
    )

    return running_days