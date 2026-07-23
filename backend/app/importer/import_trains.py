import uuid

from sqlalchemy.exc import IntegrityError

from app.database.database import SessionLocal
from app.importer.utils import load_json
from app.models.train import Train


BATCH_SIZE = 1000


def import_trains():
    db = SessionLocal()

    try:
        print("\nLoading trains.json...")

        data = load_json("trains.json")
        features = data["features"]

        print(f"Found {len(features)} trains.\n")

        inserted = 0
        skipped = 0
        batch = []

        # Existing train numbers
        existing_numbers = {
            train[0]
            for train in db.query(Train.TrainNumber).all()
        }

        for feature in features:

            props = feature.get("properties", {})

            train_number = str(props.get("number", "")).strip()

            if not train_number:
                skipped += 1
                continue

            if train_number in existing_numbers:
                skipped += 1
                continue

            train = Train(
                TrainID=uuid.uuid4(),
                TrainNumber=train_number,
                TrainName=props.get("name", "").strip(),
                TrainType=props.get("type", "").strip(),
                RailwayZone=props.get("zone", "").strip(),
                IsActive=True
            )

            batch.append(train)
            existing_numbers.add(train_number)

            if len(batch) >= BATCH_SIZE:
                db.bulk_save_objects(batch)
                db.commit()

                inserted += len(batch)
                print(f"Imported {inserted} trains...")

                batch.clear()

        if batch:
            db.bulk_save_objects(batch)
            db.commit()

            inserted += len(batch)

        print("\n===================================")
        print("Train Import Completed")
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
    import_trains()