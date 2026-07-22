from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.train import Train
from app.schemas.train_schema import TrainCreate, TrainResponse

router = APIRouter(prefix="/trains", tags=["Trains"])


@router.post("/", response_model=TrainResponse)
def create_train(train: TrainCreate, db: Session = Depends(get_db)):
    new_train = Train(**train.model_dump())
    db.add(new_train)
    db.commit()
    db.refresh(new_train)
    return new_train


@router.get("/", response_model=list[TrainResponse])
def get_trains(db: Session = Depends(get_db)):
    return db.query(Train).all()