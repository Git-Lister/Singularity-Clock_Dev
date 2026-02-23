from fastapi import APIRouter

router = APIRouter()

@router.get("/current")
async def get_current():
    # TODO: return current composite value
    return {"data_hand": 42.0, "vibe_hand": 50.0}
