from pydantic import BaseModel


class RouteCreate(BaseModel):
    TrainNumber: str
    StationCode: str
    StationSequence: int
    ArrivalTime: str
    DepartureTime: str
    Distance: int
    IsTechnicalStop: bool = False


class RouteResponse(RouteCreate):
    class Config:
        from_attributes = True