from pydantic import BaseModel


class TrainStopResponse(BaseModel):
    StationCode: str
    StationName: str
    ArrivalTime: str | None = None
    DepartureTime: str | None = None
    DayNumber: int | None = None

    class Config:
        from_attributes = True