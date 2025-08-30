# === Core ===
from fastapi import APIRouter, Request, Response
from utils.abc import clicks

router = APIRouter()

@router.get("/click")
async def auth(request: Request):
    return {"count": clicks.root.count}

@router.post("/click")
async def auth(request: Request):
    host = request.client.host if request.client else None
    clicks.addCount(1, host)