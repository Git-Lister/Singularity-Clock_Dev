import os
from pathlib import Path

# Define the project root (current working directory)
root = Path.cwd()

# Define the full directory structure as per DESIGN.md
structure = {
    "backend/app/__init__.py": "",
    "backend/app/main.py": """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Singularity Clock API"}
""",
    "backend/app/routes/clock.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/current")
async def get_current():
    # TODO: return current composite value
    return {"data_hand": 42.0, "vibe_hand": 50.0}
""",
    "backend/app/services/data_fetcher.py": """# Functions to fetch Epoch AI and arXiv data
def fetch_epoch_compute():
    # TODO
    pass

def fetch_epoch_capabilities():
    # TODO
    pass

def fetch_arxiv_counts():
    # TODO
    pass
""",
    "backend/app/services/normalizer.py": """# Min-max scaling and weighting logic
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) * 100

def composite(data):
    # TODO: apply weights 50/35/15
    pass
""",
    "backend/app/services/data_store.py": """# Read/write JSON data files
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.parent / "data"

def read_current():
    with open(DATA_DIR / "current.json") as f:
        return json.load(f)

def write_current(data):
    with open(DATA_DIR / "current.json", "w") as f:
        json.dump(data, f, indent=2)
""",
    "backend/app/models/schemas.py": """from pydantic import BaseModel
from datetime import datetime

class ClockResponse(BaseModel):
    data_hand: float
    vibe_hand: float
    timestamp: datetime
""",
    "backend/data/current.json": '{"data_hand": 42.0, "vibe_hand": 50.0, "timestamp": "2026-02-23T00:00:00"}',
    "backend/data/history.json": '[]',
    "backend/scripts/update_data.py": """#!/usr/bin/env python
# Script to fetch fresh data and update current.json / history.json
from backend.app.services import data_fetcher, normalizer, data_store

def main():
    # TODO: fetch data, compute composite, store
    pass

if __name__ == "__main__":
    main()
""",
    "backend/requirements.txt": """fastapi
uvicorn
requests
pandas
arxiv
apscheduler
pytest
""",
    "backend/README.md": "# AI Singularity Clock - Backend\n\nData fetching and API.",
    "frontend/public/index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Singularity Clock</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="app">
        <h1>Singularity Clock</h1>
        <canvas id="clock" width="400" height="400"></canvas>
    </div>
    <script src="clock.js"></script>
</body>
</html>
""",
    "frontend/public/style.css": """body {
    font-family: sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: #f0f0f0;
}
#clock {
    background: white;
    border-radius: 50%;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
}
""",
    "frontend/public/clock.js": """// Clock rendering logic
const canvas = document.getElementById('clock');
const ctx = canvas.getContext('2d');

function drawClock(dataHand, sentimentHand, vibeHand) {
    // TODO: draw clock face and hands
    console.log('Drawing clock...');
}

// On load, fetch data and draw
fetch('/api/current')
    .then(r => r.json())
    .then(data => {
        // For now, just draw with placeholder values
        drawClock(42, 30, 50);
    });
""",
    "frontend/package.json": """{
  "name": "singularity-clock-frontend",
  "version": "1.0.0",
  "description": "Frontend for AI Singularity Clock",
  "scripts": {
    "start": "npx http-server public"
  },
  "dependencies": {},
  "devDependencies": {
    "http-server": "^14.1.1"
  }
}
""",
    "docs/DESIGN.md": "# AI Singularity Clock Design Document\n\n[Content from our DESIGN.md will be placed here later]",
    ".gitignore": """# Python
__pycache__/
*.py[cod]
*.so
.Python
env/
venv/
.env
*.egg-info/
dist/
build/

# Frontend
node_modules/
npm-debug.log*

# OS
.DS_Store
Thumbs.db

# Project specific
backend/data/*.json
!backend/data/current.json  # keep placeholder
""",
    "README.md": "# AI Singularity Clock\n\n[Project overview and instructions]"
}

# Create directories and files
for filepath, content in structure.items():
    full_path = root / filepath
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {full_path}")

print("\n✅ Project structure created successfully!")
print("Next steps: create a virtual environment and install dependencies.")