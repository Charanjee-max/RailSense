import uuid
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base


class TrainStop(Base):
    __tablename__ = "train_stops"

    StopID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    TrainNumber = Column(String(20), nullable=False)
    StationCode = Column(String(20), nullable=False)

    ArrivalTime = Column(String(20))
    DepartureTime = Column(String(20))

    DayNumber = Column(Integer)

    CreatedAt = Column(DateTime, default=datetime.utcnow)
    UpdatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)