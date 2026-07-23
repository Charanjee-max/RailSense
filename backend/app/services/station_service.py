from sqlalchemy.orm import Session

from app.crud.station import search_stations


def search_station_service(
    db: Session,
    name: str,
):
    return search_stations(db, name)