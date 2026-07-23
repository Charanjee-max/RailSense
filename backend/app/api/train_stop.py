from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.train_stop import TrainStop

router = APIRouter(prefix="/trains", tags=["Train Stops"])


@router.get("/{train_number}/stops")
def get_train_stops(train_number: str, db: Session = Depends(get_db)):

    stops = (
        db.query(TrainStop)
        .filter(TrainStop.TrainNumber == train_number)
        .all()
    )

    if not stops:
        raise HTTPException(status_code=404, detail="Train not found")

    return stops