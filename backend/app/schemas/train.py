from typing import Optional
from pydantic import BaseModel


class TrainResponse(BaseModel):
    TrainNumber: str
    TrainName: str
    TrainType: Optional[str] = None
    SourceStationCode: Optional[str] = None
    DestinationStationCode: Optional[str] = None

    class Config:
        from_attributes = True