from fastapi import FastAPI
from app.database.database import engine

app = FastAPI(
    title="RailSense API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to RailSense API 🚆"
    }

@app.get("/db-test")
def db_test():
    try:
        connection = engine.connect()
        connection.close()
        return {"status": "Database Connected Successfully ✅"}
    except Exception as e:
        return {"error": str(e)}
    from fastapi import FastAPI
from app.api.station_routes import router as station_router

app = FastAPI(title="RailSense API")

app.include_router(station_router)


@app.get("/")
def home():
    return {"message": "Welcome to RailSense API"}