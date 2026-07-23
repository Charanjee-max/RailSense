from fastapi import FastAPI
from app.database.database import engine

from app.api.station_routes import router as station_router
from app.api.train_routes import router as train_router
from app.api.route_routes import router as route_router
from app.api.search_routes import router as search_router
from app.api.train_running_days_routes import router as running_days_router

app = FastAPI(
    title="RailSense API",
    version="1.0.0"
)

app.include_router(station_router)
app.include_router(train_router)
app.include_router(route_router)
app.include_router(search_router)
app.include_router(running_days_router)


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