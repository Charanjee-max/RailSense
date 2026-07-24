from sqlalchemy.orm import Session

from app.crud.train_stop import get_train_stops


def get_train_stops_service(
    db: Session,
    train_number: str
):
    return get_train_stops(
        db=db,
        train_number=train_number
    )