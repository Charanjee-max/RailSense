from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.route import Route
from app.schemas.route_schema import RouteCreate, RouteResponse

router = APIRouter(prefix="/routes", tags=["Routes"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=RouteResponse)
def create_route(route: RouteCreate, db: Session = Depends(get_db)):
    db_route = Route(**route.model_dump())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route


@router.get("/", response_model=list[RouteResponse])
def get_routes(db: Session = Depends(get_db)):
    return db.query(Route).all()