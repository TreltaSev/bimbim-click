import asyncio
from typing import Any
from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect

from utils.abc import clicks
from utils.console import console

router = APIRouter()

class ConnectionState:
    def __init__(self):
        self.count: int = clicks.root.count


async def listener(websocket: WebSocket, state: ConnectionState):
    while True:
        data: dict[str, Any] = await websocket.receive_json()
        operation = data.get("operation")

        if not operation:
            continue

        match operation:
            case "click":
                try:
                    state.count += 1
                    clicks.addCount(1)
                    await websocket.send_json({"operation": "click", "ok": True})
                except Exception:
                    await websocket.send_json({"operation": "click", "ok": False})


async def talker(websocket: WebSocket, state: ConnectionState):
    while True:
        await asyncio.sleep(0.1)
        if state.count < clicks.root.count:
            delta = clicks.root.count - state.count
            state.count = clicks.root.count
            await websocket.send_json({"operation": "update", "delta": delta})


@router.websocket("/click")
async def click_ws(websocket: WebSocket):
    await websocket.accept()
    state = ConnectionState()
    try:
        await asyncio.gather(listener(websocket, state), talker(websocket, state))
    except WebSocketDisconnect:
        console.info("Client Disconnect")
    except Exception:
        console.print_exception()


@router.get("/click")
async def get_clicks(_: Request):
    return {"total": clicks.root.count}


@router.post("/click")
async def post_click(request: Request):
    host = request.client.host if request.client else None
    clicks.addCount(1, host)
    return {"ok": True, "total": clicks.root.count}
