import uuid
from sqlalchemy import Column, String, Integer, Boolean
from app.database.database import Base


class Route(Base):
    __tablename__ = "routes"

    RouteID = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    TrainNumber = Column(String, nullable=False)
    StationCode = Column(String, nullable=False)

    StationSequence = Column(Integer, nullable=False)

    ArrivalTime = Column(String)
    DepartureTime = Column(String)

    Distance = Column(Integer, default=0)
    DayNumber = Column(Integer, default=1)

    IsSource = Column(Boolean, default=False)
    IsDestination = Column(Boolean, default=False)
    IsTechnicalStop = Column(Boolean, default=False)