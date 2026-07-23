from pydantic import BaseModel
from typing import Optional


class TrainStopResponse(BaseModel):
    TrainNumber: str
    StationCode: str
    ArrivalTime: Optional[str]
    DepartureTime: Optional[str]
    DayNumber: Optional[int]

    class Config:
        from_attributes = True