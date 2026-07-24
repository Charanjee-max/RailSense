from fastapi import FastAPI

from app.api.dashboard import router as dashboard_router
from app.api.running_days import router as running_days_router
from app.api.station import router as station_router
from app.api.train import router as train_router
from app.api.train_stop import router as train_stop_router

from app.exceptions.handlers import register_exception_handlers

app = FastAPI(
    title="RailSense API",
    version="1.0.0",
)

# Register global exception handlers
register_exception_handlers(app)

# Register API routers
app.include_router(dashboard_router)
app.include_router(train_router)
app.include_router(station_router)
app.include_router(train_stop_router)
app.include_router(running_days_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to RailSense API"
    }