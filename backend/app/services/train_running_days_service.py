from sqlalchemy.orm import Session

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
    return create_running_days(
        db=db,
        data=data,
    )


def get_all_running_days_service(
    db: Session,
):
    return get_all_running_days(
        db=db,
    )


def get_running_days_by_train_service(
    db: Session,
    train_number: str,
):
    running_days = get_running_days_by_train(
        db=db,
        train_number=train_number,
    )

    if not running_days:
        raise ResourceNotFoundException(
            f"Running days not found for train '{train_number}'."
        )

    return running_days