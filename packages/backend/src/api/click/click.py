# === Core ===
from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/click")
async def auth(request: Request):
    if request.client:
        print(request.client.host)
    return {"count": 29731}

@router.post("/click")
async def auth(request: Request):
    return {"ok": True}