from sqlalchemy.orm import Session

from app.models.train_stop import TrainStop
from app.models.station import Station


def get_train_stops(db: Session, train_number: str):

    stops = (
        db.query(
            TrainStop.StationCode,
            Station.StationName,
            TrainStop.ArrivalTime,
            TrainStop.DepartureTime,
            TrainStop.DayNumber
        )
        .join(
            Station,
            TrainStop.StationCode == Station.StationCode
        )
        .filter(
            TrainStop.TrainNumber == train_number
        )
        .order_by(
            TrainStop.DayNumber,
            TrainStop.DepartureTime
        )
        .all()
    )

    return stops