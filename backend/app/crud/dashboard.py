from sqlalchemy.orm import Session

from app.models.station import Station
from app.models.train import Train
from app.models.train_stop import TrainStop


def get_dashboard_stats(db: Session):

    return {
        "totalStations": db.query(Station).count(),
        "totalTrains": db.query(Train).count(),
        "totalTrainStops": db.query(TrainStop).count(),
        "activeTrains": db.query(Train).filter(Train.IsActive == True).count(),
        "activeStations": db.query(Station).filter(Station.IsActive == True).count(),
    }