from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.train import TrainResponse
from app.schemas.train_detail import TrainDetailResponse

from app.services.train_service import (
    search_train_service,
    get_train_details,
)

router = APIRouter(
    prefix="/trains",
    tags=["Trains"],
)


@router.get(
    "/search",
    response_model=List[TrainResponse]
)
def search_trains(
    number: str | None = Query(None),
    name: str | None = Query(None),
    db: Session = Depends(get_db),
):
    return search_train_service(
        db=db,
        number=number,
        name=name,
    )


@router.get(
    "/{train_number}",
    response_model=TrainDetailResponse
)
def get_train(
    train_number: str,
    db: Session = Depends(get_db),
):

    train = get_train_details(db, train_number)

    if not train:
        raise HTTPException(
            status_code=404,
            detail="Train not found"
        )

    return train