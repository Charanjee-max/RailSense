from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.dashboard import DashboardStatsResponse
from app.services.dashboard_service import dashboard_stats_service

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/stats",
    response_model=DashboardStatsResponse
)
def get_dashboard(
    db: Session = Depends(get_db)
):
    return dashboard_stats_service(db)