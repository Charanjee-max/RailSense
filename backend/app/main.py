from fastapi import FastAPI
from app.database.database import engine

from app.api.dashboard import router as dashboard_router
from app.api.running_days import router as running_days_router
from app.api.station import router as station_router
from app.api.train import router as train_router
from app.api.train_stop import router as train_stop_router

app = FastAPI(
    title="RailSense API",
    version="1.0.0"
)

app.include_router(station_router)
app.include_router(train_router)
app.include_router(train_stop_router)
app.include_router(running_days_router)
app.include_router(dashboard_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to RailSense API"
    }


@app.get("/db-test")
def db_test():
    try:
        connection = engine.connect()
        connection.close()
        return {
            "status": "Database Connected Successfully ✅"
        }
    except Exception as e:
        return {
            "error": str(e)
        }