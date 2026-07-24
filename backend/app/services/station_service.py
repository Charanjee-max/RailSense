from sqlalchemy.orm import Session

from app.crud.station import (
    create_station,
    get_all_stations,
    search_stations,
)

from app.exceptions.custom_exceptions import (
    ResourceNotFoundException,
    BadRequestException,
    ConflictException,
)


def create_station_service(
    db: Session,
    station,
):
    return create_station(
        db=db,
        station=station,
    )


def get_all_stations_service(
    db: Session,
):
    return get_all_stations(
        db=db,
    )


def search_station_service(
    db: Session,
    name: str,
):
    return search_stations(
        db=db,
        name=name,
    )