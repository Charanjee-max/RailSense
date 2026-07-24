from typing import Optional

from pydantic import BaseModel


class StationCreate(BaseModel):
    StationCode: str
    StationName: str
    State: str
    RailwayZone: str
    Division: str
    IsJunction: bool = False
    IsTerminal: bool = False


class StationResponse(BaseModel):
    StationCode: str
    StationName: str
    RailwayZone: Optional[str] = None
    State: Optional[str] = None

    class Config:
        from_attributes = True