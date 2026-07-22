from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.database.database import Base
import uuid
from datetime import datetime


class Train(Base):
    __tablename__ = "trains"

    TrainID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    TrainNumber = Column(String(10), unique=True, nullable=False)
    TrainName = Column(String(100), nullable=False)
    TrainType = Column(String(50))
    RailwayZone = Column(String(20))
    IsActive = Column(Boolean, default=True)
    CreatedAt = Column(DateTime, default=datetime.utcnow)
    UpdatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    