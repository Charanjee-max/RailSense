from typing import Optional
from pydantic import BaseModel


class StationResponse(BaseModel):
    StationCode: str
    StationName: str
    RailwayZone: Optional[str] = None
    State: Optional[str] = None

    class Config:
        from_attributes = True