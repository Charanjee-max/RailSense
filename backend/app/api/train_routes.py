from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.train import Train
from app.models.route import Route
from app.schemas.train_schema import TrainCreate, TrainResponse

router = APIRouter(prefix="/trains", tags=["Trains"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TrainResponse)
def create_train(train: TrainCreate, db: Session = Depends(get_db)):
    db_train = Train(**train.model_dump())
    db.add(db_train)
    db.commit()
    db.refresh(db_train)
    return db_train


@router.get("/", response_model=list[TrainResponse])
def get_trains(db: Session = Depends(get_db)):
    return db.query(Train).all()


@router.get("/station/{station_code}")
def get_trains_by_station(station_code: str, db: Session = Depends(get_db)):
    routes = db.query(Route).filter(Route.StationCode == station_code).all()

    result = []

    for route in routes:
        train = db.query(Train).filter(
            Train.TrainNumber == route.TrainNumber
        ).first()

        if train:
            result.append({
                "TrainNumber": train.TrainNumber,
                "TrainName": train.TrainName,
                "TrainType": train.TrainType,
                "StationCode": station_code
            })

    return result