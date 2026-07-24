from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.train_running_days_schema import (
    TrainRunningDaysCreate,
    TrainRunningDaysResponse,
)

from app.services.train_running_days_service import (
    create_running_days_service,
    get_all_running_days_service,
    get_running_days_by_train_service,
)

router = APIRouter(
    prefix="/running-days",
    tags=["Running Days"],
)


@router.post(
    "/",
    response_model=TrainRunningDaysResponse,
)
def create_running_days(
    data: TrainRunningDaysCreate,
    db: Session = Depends(get_db),
):
    return create_running_days_service(
        db=db,
        data=data,
    )


@router.get(
    "/",
    response_model=List[TrainRunningDaysResponse],
)
def get_running_days(
    db: Session = Depends(get_db),
):
    return get_all_running_days_service(
        db=db,
    )


@router.get(
    "/{train_number}",
    response_model=TrainRunningDaysResponse,
)
def get_running_days_by_train(
    train_number: str,
    db: Session = Depends(get_db),
):
    running_days = get_running_days_by_train_service(
        db=db,
        train_number=train_number,
    )

    if not running_days:
        raise HTTPException(
            status_code=404,
            detail="Train running days not found.",
        )

    return running_days