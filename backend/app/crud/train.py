from sqlalchemy.orm import Session

from app.models.train import Train
from app.models.train_running_days import TrainRunningDays
from app.models.train_stop import TrainStop


def create_train(
    db: Session,
    train,
):
    db_train = Train(**train.model_dump())

    db.add(db_train)
    db.commit()
    db.refresh(db_train)

    return db_train


def get_all_trains(
    db: Session,
):
    return (
        db.query(Train)
        .all()
    )


def search_trains(
    db: Session,
    number: str | None = None,
    name: str | None = None,
):
    query = db.query(Train)

    if number:
        query = query.filter(
            Train.TrainNumber.ilike(f"%{number}%")
        )

    if name:
        query = query.filter(
            Train.TrainName.ilike(f"%{name}%")
        )

    return query.all()


def get_train_by_number(
    db: Session,
    train_number: str,
):
    return (
        db.query(Train)
        .filter(Train.TrainNumber == train_number)
        .first()
    )


def get_running_days(
    db: Session,
    train_number: str,
):
    return (
        db.query(TrainRunningDays)
        .filter(TrainRunningDays.TrainNumber == train_number)
        .first()
    )


def get_total_stops(
    db: Session,
    train_number: str,
):
    return (
        db.query(TrainStop)
        .filter(TrainStop.TrainNumber == train_number)
        .count()
    )