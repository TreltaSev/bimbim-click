# === Core ===
import click
from fastapi import APIRouter, Request, Response
from utils.abc import clicks

router = APIRouter()

@router.get("/click")
async def auth(request: Request):
    response = {
        "total": clicks.root.count
    }
    
    forwarded_for = request.headers.get("x-forwarded-for")
    print(forwarded_for)
    
    ip = forwarded_for.split(",")[0].strip()
    if ip.startswith("::ffff:"):
        ip = ip.replace("::ffff:", "")
    
    
    ipCount = 0    
    _obj = clicks.discover.get_ip(ip)
    if _obj:
        print("got obj", _obj)
        ipCount = _obj.count
        
    
    response["ip"] = ipCount
    
    return response

@router.post("/click")
async def auth(request: Request):
    host = request.client.host if request.client else None
    clicks.addCount(1, host)