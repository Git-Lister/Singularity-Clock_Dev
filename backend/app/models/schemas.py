from pydantic import BaseModel
from datetime import datetime

class ClockResponse(BaseModel):
    data_hand: float
    vibe_hand: float
    timestamp: datetime
