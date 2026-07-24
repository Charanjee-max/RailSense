from sqlalchemy.orm import Session

from app.crud.train import (
    create_train,
    get_all_trains,
    search_trains,
    get_train_by_number,
    get_running_days,
    get_total_stops,
)

from app.exceptions.custom_exceptions import (
    ResourceNotFoundException,
)


def create_train_service(
    db: Session,
    train,
):
    return create_train(
        db=db,
        train=train,
    )


def get_all_trains_service(
    db: Session,
):
    return get_all_trains(
        db=db,
    )


def search_train_service(
    db: Session,
    number: str | None = None,
    name: str | None = None,
):
    return search_trains(
        db=db,
        number=number,
        name=name,
    )


def get_train_details(
    db: Session,
    train_number: str,
):
    train = get_train_by_number(db, train_number)

    if not train:
        raise ResourceNotFoundException(
            f"Train '{train_number}' not found."
        )

    running = get_running_days(db, train_number)

    running_days = []

    if running:
        if running.Monday:
            running_days.append("Monday")
        if running.Tuesday:
            running_days.append("Tuesday")
        if running.Wednesday:
            running_days.append("Wednesday")
        if running.Thursday:
            running_days.append("Thursday")
        if running.Friday:
            running_days.append("Friday")
        if running.Saturday:
            running_days.append("Saturday")
        if running.Sunday:
            running_days.append("Sunday")

    return {
        "TrainNumber": train.TrainNumber,
        "TrainName": train.TrainName,
        "TrainType": train.TrainType,
        "RailwayZone": train.RailwayZone,
        "RunningDays": running_days,
        "TotalStops": get_total_stops(db, train_number),
    }