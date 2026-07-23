from typing import List, Optional

from pydantic import BaseModel


class TrainDetailResponse(BaseModel):
    TrainNumber: str
    TrainName: str
    TrainType: Optional[str] = None
    RailwayZone: Optional[str] = None
    RunningDays: List[str]
    TotalStops: int