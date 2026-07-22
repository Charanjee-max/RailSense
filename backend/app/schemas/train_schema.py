from pydantic import BaseModel


class TrainCreate(BaseModel):
    TrainNumber: str
    TrainName: str
    TrainType: str
    RailwayZone: str


class TrainResponse(TrainCreate):
    class Config:
        from_attributes = True