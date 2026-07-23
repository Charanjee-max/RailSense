from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.database.database import Base
import uuid
from datetime import datetime


class Station(Base):
    __tablename__ = "stations"

    StationID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    StationCode = Column(String(20), unique=True, nullable=False)
    StationName = Column(String(100), nullable=False)
    State = Column(String(50))
    RailwayZone = Column(String(20))
    Division = Column(String(50))
    IsJunction = Column(Boolean, default=False)
    IsTerminal = Column(Boolean, default=False)
    IsActive = Column(Boolean, default=True)
    CreatedAt = Column(DateTime, default=datetime.utcnow)
    UpdatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)