from sqlalchemy.orm import Session

from app.models.station import Station


def create_station(
    db: Session,
    station,
):
    db_station = Station(**station.model_dump())

    db.add(db_station)
    db.commit()
    db.refresh(db_station)

    return db_station


def get_all_stations(
    db: Session,
):
    return (
        db.query(Station)
        .all()
    )


def search_stations(
    db: Session,
    name: str,
):
    return (
        db.query(Station)
        .filter(
            Station.StationName.ilike(f"%{name}%")
        )
        .order_by(Station.StationName)
        .limit(20)
        .all()
    )