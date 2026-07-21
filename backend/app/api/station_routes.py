from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.station import Station
from app.schemas.station_schema import StationCreate, StationResponse

router = APIRouter(prefix="/stations", tags=["Stations"])


@router.post("/", response_model=StationResponse)
def create_station(station: StationCreate, db: Session = Depends(get_db)):
    new_station = Station(**station.model_dump())
    db.add(new_station)
    db.commit()
    db.refresh(new_station)
    return new_station


@router.get("/", response_model=list[StationResponse])
def get_stations(db: Session = Depends(get_db)):
    return db.query(Station).all()