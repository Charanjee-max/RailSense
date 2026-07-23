import uuid
from sqlalchemy import Column, String, Boolean
from app.database.database import Base


class TrainRunningDays(Base):
    __tablename__ = "train_running_days"

    RunningDayID = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    TrainNumber = Column(String, nullable=False, unique=True)
    Monday = Column(Boolean, default=False)
    Tuesday = Column(Boolean, default=False)
    Wednesday = Column(Boolean, default=False)
    Thursday = Column(Boolean, default=False)
    Friday = Column(Boolean, default=False)
    Saturday = Column(Boolean, default=False)
    Sunday = Column(Boolean, default=False)