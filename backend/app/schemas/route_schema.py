from pydantic import BaseModel


class RouteCreate(BaseModel):
    TrainNumber: str
    StationCode: str
    StationSequence: int
    ArrivalTime: str
    DepartureTime: str
    Distance: int = 0
    IsSource: bool = False
    IsDestination: bool = False
    IsTechnicalStop: bool = False


class RouteResponse(RouteCreate):
    class Config:
        from_attributes = True