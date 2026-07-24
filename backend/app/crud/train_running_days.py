from sqlalchemy.orm import Session

from app.models.train_running_days import TrainRunningDays


def create_running_days(
    db: Session,
    data
):
    db_data = TrainRunningDays(**data.model_dump())

    db.add(db_data)
    db.commit()
    db.refresh(db_data)

    return db_data


def get_all_running_days(
    db: Session
):
    return (
        db.query(TrainRunningDays)
        .all()
    )


def get_running_days_by_train(
    db: Session,
    train_number: str
):
    return (
        db.query(TrainRunningDays)
        .filter(
            TrainRunningDays.TrainNumber == train_number
        )
        .first()
    )