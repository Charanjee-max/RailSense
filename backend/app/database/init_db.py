from app.database.database import engine, Base

# Import all models
from app.models.station import Station
from app.models.train import Train
from app.models.route import Route
from app.models.train_running_days import TrainRunningDays

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")