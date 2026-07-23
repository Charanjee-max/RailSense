from pydantic import BaseModel


class DashboardStatsResponse(BaseModel):
    totalStations: int
    totalTrains: int
    totalTrainStops: int
    activeTrains: int
    activeStations: int