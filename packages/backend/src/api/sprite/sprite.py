# === Core ===
import os
import base64
import pathlib
from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, Response, status
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/sprites")
async def sprites(response: Response):
    out_dirs = []
    dir_path = "/sprites"
    if os.path.exists(dir_path):
        for filename in os.listdir(dir_path):
            if filename.lower().endswith(".png"):
                out_dirs.append(filename)

    response.status_code = 200
    return out_dirs

@router.get("/sprites/{sprite_name}")
async def sprites_query(response: Response, sprite_name: Annotated[str, Path()]):
    
    image_path = pathlib.Path(f"/sprites/{sprite_name}")
    if not image_path.exists:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Sprite with name {sprite_name} doesn't exist")
    
    response.media_type = "image/png"
    
    return FileResponse(
        image_path,
        media_type="image/png",
        headers={"Content-Disposition": f"inline; filename={image_path.name}"}
    )