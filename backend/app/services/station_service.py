from sqlalchemy.orm import Session

from app.core.logger import logger

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
    logger.info(
        f"Creating station: {station.StationCode}"
    )

    created_station = create_station(
        db=db,
        station=station,
    )

    logger.info(
        f"Station created successfully: {created_station.StationCode}"
    )

    return created_station


def get_all_stations_service(
    db: Session,
):
    logger.info("Fetching all stations")

    stations = get_all_stations(
        db=db,
    )

    logger.info(
        f"Fetched {len(stations)} stations"
    )

    return stations


def search_station_service(
    db: Session,
    name: str,
):
    logger.info(
        f"Searching stations with name: {name}"
    )

    stations = search_stations(
        db=db,
        name=name,
    )

    logger.info(
        f"Search returned {len(stations)} station(s)"
    )

    return stations