from app.database.database import SessionLocal
from app.models.train_stop import TrainStop
from app.importer.utils import load_json


def import_train_stops():
    db = SessionLocal()

    try:
        data = load_json("schedules.json")

        print(f"Found {len(data)} train stop records.")

        inserted = 0
        skipped = 0
        batch = []

        # Existing records
        existing = {
            (x.TrainNumber, x.StationCode, x.ArrivalTime, x.DepartureTime)
            for x in db.query(TrainStop).all()
        }

        for row in data:

            arrival = None if row.get("arrival") == "None" else row.get("arrival")
            departure = None if row.get("departure") == "None" else row.get("departure")

            key = (
                row.get("train_number"),
                row.get("station_code"),
                arrival,
                departure,
            )

            if key in existing:
                skipped += 1
                continue

            batch.append(
                TrainStop(
                    TrainNumber=row.get("train_number"),
                    StationCode=row.get("station_code"),
                    ArrivalTime=arrival,
                    DepartureTime=departure,
                    DayNumber=row.get("day"),
                )
            )

            existing.add(key)
            inserted += 1

            if len(batch) >= 1000:
                db.bulk_save_objects(batch)
                db.commit()
                batch.clear()
                print(f"Inserted {inserted} records...")

        if batch:
            db.bulk_save_objects(batch)
            db.commit()

        print("\nImport Completed")
        print(f"Inserted : {inserted}")
        print(f"Skipped  : {skipped}")

    except Exception as e:
        db.rollback()
        print("Error:", e)

    finally:
        db.close()


if __name__ == "__main__":
    import_train_stops()