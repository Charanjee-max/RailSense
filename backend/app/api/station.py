from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.models.train_stop import TrainStop

from app.schemas.station import (
    StationCreate,
    StationResponse,
)

from app.services.station_service import (
    create_station_service,
    get_all_stations_service,
    search_station_service,
)

router = APIRouter(
    prefix="/stations",
    tags=["Stations"],
)


@router.post(
    "/",
    response_model=StationResponse,
)
def create_station(
    station: StationCreate,
    db: Session = Depends(get_db),
):
    return create_station_service(
        db=db,
        station=station,
    )


@router.get(
    "/",
    response_model=List[StationResponse],
)
def get_all_stations(
    db: Session = Depends(get_db),
):
    return get_all_stations_service(
        db=db,
    )


@router.get(
    "/search",
    response_model=List[StationResponse],
)
def search_station(
    name: str = Query(...),
    db: Session = Depends(get_db),
):
    return search_station_service(
        db=db,
        name=name,
    )


@router.get("/{station_code}/departures")
def get_departures(
    station_code: str,
    db: Session = Depends(get_db),
):
    departures = (
        db.query(TrainStop)
        .filter(
            TrainStop.StationCode == station_code.upper(),
            TrainStop.DepartureTime != None,
        )
        .order_by(TrainStop.DepartureTime)
        .all()
    )

    if not departures:
        raise HTTPException(
            status_code=404,
            detail="No departures found.",
        )

    return departures


@router.get("/{station_code}/arrivals")
def get_arrivals(
    station_code: str,
    db: Session = Depends(get_db),
):
    arrivals = (
        db.query(TrainStop)
        .filter(
            TrainStop.StationCode == station_code.upper(),
            TrainStop.ArrivalTime != None,
        )
        .order_by(TrainStop.ArrivalTime)
        .all()
    )

    if not arrivals:
        raise HTTPException(
            status_code=404,
            detail="No arrivals found.",
        )

    return arrivals