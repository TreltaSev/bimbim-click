# === Core ===
import os
import pathlib
from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, Response, status
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/meows")
async def meows(response: Response):
    out_dirs = []
    dir_path = "/meow"
    if os.path.exists(dir_path):
        for filename in os.listdir(dir_path):
            if filename.lower().endswith(".mp3"):
                out_dirs.append(filename)

    response.status_code = 200
    return out_dirs

@router.get("/meows/{meow_name}")
async def meows_query(response: Response, meow_name: Annotated[str, Path()]):
    
    image_path = pathlib.Path(f"/meow/{meow_name}")
    if not image_path.exists:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Meow with name {meow_name} doesn't exist")
    
    response.media_type = "audio/mpeg"
    
    return FileResponse(
        image_path,
        media_type=response.media_type,
        headers={"Content-Disposition": f"inline; filename={image_path.name}"}
    )