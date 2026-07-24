from sqlalchemy.orm import Session

from app.crud.train_running_days import (
    create_running_days,
    get_all_running_days,
    get_running_days_by_train,
)


def create_running_days_service(
    db: Session,
    data
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
    return get_running_days_by_train(
        db=db,
        train_number=train_number,
    )