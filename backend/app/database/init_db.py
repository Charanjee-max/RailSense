from app.database.database import engine, Base

# Import all models
from app.models.station import Station

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")