from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.train import Train
from app.models.route import Route
from app.schemas.train_schema import TrainCreate, TrainResponse

router = APIRouter(
    prefix="/trains",
    tags=["Trains"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# Create Train
# -----------------------------
@router.post("/", response_model=TrainResponse)
def create_train(train: TrainCreate, db: Session = Depends(get_db)):

    existing_train = (
        db.query(Train)
        .filter(Train.TrainNumber == train.TrainNumber)
        .first()
    )

    if existing_train:
        raise HTTPException(
            status_code=400,
            detail="Train already exists."
        )

    db_train = Train(**train.model_dump())

    db.add(db_train)
    db.commit()
    db.refresh(db_train)

    return db_train


# -----------------------------
# Get All Trains
# -----------------------------
@router.get("/", response_model=list[TrainResponse])
def get_trains(db: Session = Depends(get_db)):
    return db.query(Train).all()


# -----------------------------
# Get Train by Number
# -----------------------------
@router.get("/{train_number}", response_model=TrainResponse)
def get_train(train_number: str, db: Session = Depends(get_db)):

    train = (
        db.query(Train)
        .filter(Train.TrainNumber == train_number)
        .first()
    )

    if not train:
        raise HTTPException(
            status_code=404,
            detail="Train not found."
        )

    return train


# -----------------------------
# Get Trains Passing Through a Station
# -----------------------------
@router.get("/station/{station_code}")
def get_trains_by_station(
    station_code: str,
    db: Session = Depends(get_db)
):

    routes = (
        db.query(Route)
        .filter(Route.StationCode == station_code)
        .all()
    )

    if not routes:
        raise HTTPException(
            status_code=404,
            detail="No trains found for this station."
        )

    result = []

    for route in routes:

        train = (
            db.query(Train)
            .filter(Train.TrainNumber == route.TrainNumber)
            .first()
        )

        if train:
            result.append({
                "TrainNumber": train.TrainNumber,
                "TrainName": train.TrainName,
                "TrainType": train.TrainType,
                "RailwayZone": train.RailwayZone,
                "StationCode": station_code,
                "StationSequence": route.StationSequence,
                "ArrivalTime": route.ArrivalTime,
                "DepartureTime": route.DepartureTime,
                "Distance": route.Distance,
                "DayNumber": route.DayNumber
            })

    return result