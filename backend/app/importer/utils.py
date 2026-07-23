import json
from pathlib import Path


def load_json(filename: str):
    """
    Load a JSON file from the backend/data folder.
    """

    data_path = Path("data") / filename

    if not data_path.exists():
        raise FileNotFoundError(f"File not found: {data_path}")

    with open(data_path, "r", encoding="utf-8") as file:
        return json.load(file)