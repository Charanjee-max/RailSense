import uuid

from sqlalchemy.exc import IntegrityError

from app.database.database import SessionLocal
from app.importer.utils import load_json
from app.models.station import Station


BATCH_SIZE = 1000


def import_stations():
    db = SessionLocal()

    try:
        print("\nLoading stations.json...")
        data = load_json("stations.json")

        features = data["features"]

        print(f"Found {len(features)} stations.\n")

        inserted = 0
        skipped = 0
        batch = []

        # Existing station codes
        existing_codes = {
            code[0]
            for code in db.query(Station.StationCode).all()
        }

        for feature in features:

            props = feature.get("properties", {})

            station_code = str(props.get("code", "")).strip()

            if not station_code:
                skipped += 1
                continue

            if station_code in existing_codes:
                skipped += 1
                continue

            station = Station(
                StationID=uuid.uuid4(),
                StationCode=station_code,
                StationName=props.get("name"),
                State=props.get("state"),
                RailwayZone=props.get("zone"),
                Division=None,
                IsJunction=False,
                IsTerminal=False,
                IsActive=True
            )

            batch.append(station)
            existing_codes.add(station_code)

            if len(batch) >= BATCH_SIZE:
                db.bulk_save_objects(batch)
                db.commit()

                inserted += len(batch)

                print(f"Imported {inserted} stations...")

                batch.clear()

        if batch:
            db.bulk_save_objects(batch)
            db.commit()

            inserted += len(batch)

        print("\n===================================")
        print("Stations Import Completed")
        print("===================================")
        print(f"Inserted : {inserted}")
        print(f"Skipped  : {skipped}")
        print("===================================\n")

    except IntegrityError as e:
        db.rollback()
        print("Database Error:", e)

    except Exception as e:
        db.rollback()
        print("Error:", e)

    finally:
        db.close()


if __name__ == "__main__":
    import_stations()