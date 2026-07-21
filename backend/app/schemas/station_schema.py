from pydantic import BaseModel


class StationCreate(BaseModel):
    StationCode: str
    StationName: str
    State: str
    RailwayZone: str
    Division: str
    IsJunction: bool = False
    IsTerminal: bool = False


class StationResponse(StationCreate):
    class Config:
        from_attributes = True