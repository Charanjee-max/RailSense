from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.train_running_days import TrainRunningDays
from app.schemas.train_running_days_schema import (
    TrainRunningDaysCreate,
    TrainRunningDaysResponse,
)

router = APIRouter(prefix="/running-days", tags=["Running Days"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TrainRunningDaysResponse)
def create_running_days(data: TrainRunningDaysCreate, db: Session = Depends(get_db)):
    db_data = TrainRunningDays(**data.model_dump())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


@router.get("/", response_model=list[TrainRunningDaysResponse])
def get_running_days(db: Session = Depends(get_db)):
    return db.query(TrainRunningDays).all()


@router.get("/{train_number}", response_model=TrainRunningDaysResponse)
def get_running_days_by_train(train_number: str, db: Session = Depends(get_db)):
    return (
        db.query(TrainRunningDays)
        .filter(TrainRunningDays.TrainNumber == train_number)
        .first()
    )