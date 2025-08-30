# === Core ===
from fastapi import APIRouter

router = APIRouter()

@router.get("/click")
async def auth():
    return {"count": 29731}

@router.post("/click")
async def auth():
    return {"ok": True}