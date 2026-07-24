from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.train_stop import TrainStopResponse
from app.services.train_stop_service import get_train_stops_service

router = APIRouter(
    prefix="/trains",
    tags=["Train Stops"]
)


@router.get(
    "/{train_number}/stops",
    response_model=List[TrainStopResponse]
)
def get_train_stops(
    train_number: str,
    db: Session = Depends(get_db)
):

    stops = get_train_stops_service(
        db=db,
        train_number=train_number
    )

    if not stops:
        raise HTTPException(
            status_code=404,
            detail="Train not found."
        )

    return stops