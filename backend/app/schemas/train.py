from typing import Optional

from pydantic import BaseModel


class TrainCreate(BaseModel):
    TrainNumber: str
    TrainName: str
    TrainType: Optional[str] = None
    RailwayZone: Optional[str] = None


class TrainResponse(TrainCreate):
    class Config:
        from_attributes = True