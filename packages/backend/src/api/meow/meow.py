# === Core ===
import os
import base64
from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/meows")
async def meows(response: Response):
    files_data = {}

    dir_path = "/meow"
    if os.path.exists(dir_path):
        for filename in os.listdir(dir_path):
            if filename.lower().endswith(".mp3"):
                file_path = os.path.join(dir_path, filename)
                try:
                    with open(file_path, "rb") as f:
                        # base64 encode the contents
                        b64_data = base64.b64encode(f.read()).decode("utf-8")
                        files_data[filename] = b64_data
                except Exception as e:
                    files_data[filename] = f"Error: {e}"

    response.status_code = 200
    return files_data
