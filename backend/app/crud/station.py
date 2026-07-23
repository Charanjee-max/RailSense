from sqlalchemy.orm import Session

from app.models.station import Station


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