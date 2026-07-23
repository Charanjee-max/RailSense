from pydantic import BaseModel


class TrainRunningDaysCreate(BaseModel):
    TrainNumber: str

    Monday: bool = False
    Tuesday: bool = False
    Wednesday: bool = False
    Thursday: bool = False
    Friday: bool = False
    Saturday: bool = False
    Sunday: bool = False


class TrainRunningDaysResponse(TrainRunningDaysCreate):
    RunningDayID: str

    class Config:
        from_attributes = True