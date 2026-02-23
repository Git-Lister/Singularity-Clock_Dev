"""Read/write JSON data files."""

import json
from pathlib import Path
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

# Get the data directory (two levels up from this file)
DATA_DIR = Path(__file__).parent.parent.parent / "data"

def ensure_data_dir():
    """Create data directory if it doesn't exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def read_current() -> Dict[str, Any]:
    """Read the current clock state from current.json."""
    current_path = DATA_DIR / "current.json"
    if not current_path.exists():
        logger.warning("current.json not found, returning empty dict")
        return {}
    
    with open(current_path, 'r') as f:
        return json.load(f)

def write_current(data: Dict[str, Any]) -> None:
    """Write the current clock state to current.json."""
    ensure_data_dir()
    current_path = DATA_DIR / "current.json"
    with open(current_path, 'w') as f:
        json.dump(data, f, indent=2, default=str)
    logger.info(f"Updated current.json")

def read_history() -> list:
    """Read historical data from history.json."""
    history_path = DATA_DIR / "history.json"
    if not history_path.exists():
        return []
    
    with open(history_path, 'r') as f:
        return json.load(f)

def append_to_history(entry: Dict[str, Any]) -> None:
    """Append an entry to history.json."""
    ensure_data_dir()
    history_path = DATA_DIR / "history.json"
    
    history = read_history()
    history.append(entry)
    
    # Keep last 1000 entries max
    if len(history) > 1000:
        history = history[-1000:]
    
    with open(history_path, 'w') as f:
        json.dump(history, f, indent=2, default=str)
    logger.info(f"Appended to history.json (total: {len(history)})")