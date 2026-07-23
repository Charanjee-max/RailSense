from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.route import Route
from app.models.train import Train

router = APIRouter(prefix="/search", tags=["Search"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def search_trains(from_station: str, to_station: str, db: Session = Depends(get_db)):
    from_routes = db.query(Route).filter(
        Route.StationCode == from_station
    ).all()

    results = []

    for from_route in from_routes:
        to_route = db.query(Route).filter(
            Route.TrainNumber == from_route.TrainNumber,
            Route.StationCode == to_station,
            Route.StationSequence > from_route.StationSequence
        ).first()

        if to_route:
            train = db.query(Train).filter(
                Train.TrainNumber == from_route.TrainNumber
            ).first()

            if train:
                results.append({
                    "TrainNumber": train.TrainNumber,
                    "TrainName": train.TrainName,
                    "TrainType": train.TrainType,
                    "From": from_station,
                    "To": to_station
                })

    return results