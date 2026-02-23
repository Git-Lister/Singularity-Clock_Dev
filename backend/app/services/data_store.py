# Read/write JSON data files
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.parent / "data"

def read_current():
    with open(DATA_DIR / "current.json") as f:
        return json.load(f)

def write_current(data):
    with open(DATA_DIR / "current.json", "w") as f:
        json.dump(data, f, indent=2)
