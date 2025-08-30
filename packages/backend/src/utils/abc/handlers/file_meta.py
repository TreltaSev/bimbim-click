# === Core ===
import io
import secrets
import random
from pathlib import Path
from fastapi import HTTPException, UploadFile, status
from pydantic import Field
import requests

# === Utils ===
from utils.abc.handlers.base import WrapperModel
from utils.helper.time import now

# === Database ===
from pymongo.collection import Collection
from utils.mongo.Client import MongoClient

# === Types ===
from typing import Any, ClassVar, Literal, Self
from utils.types import ImagesPostData


class FileMeta(WrapperModel):
    created_at: int = Field(default_factory=lambda: now())
    filename: str = Field(default_factory=str)
    tags: list[str] = Field(default_factory=list)
    id: str = Field(default_factory=lambda: secrets.token_hex(32))

    __collection__: ClassVar[Collection] = MongoClient.file_metas

    __shared_volume__: Path = Path("/shared/images")

    
    def get_file(self, mode: Literal["low", "base"] = "base") -> Path | None:
        """
        Get the file linked to this file meta object
        """
        file_path = self.__shared_volume__ / f"{self.id}.{mode}"        
        return file_path if file_path.exists() else None
    
    def delete_file(self):
        """
        Deletes the current file linked to this object.
        
        :raises HTTPException: if no image is found (404)
        """
        possible_file: Path = self.__shared_volume__ / f"{self.id}.base"
        
        if not possible_file.exists() and self.exists(id=self.id):
            self.delete()
            return
        
        if not possible_file.exists():
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Image {self.id}.base not found in file system")
        
        possible_file.unlink()

    @classmethod
    async def create_file(cls, meta: ImagesPostData, file: UploadFile, *args, **kwargs) -> Self:
        """
        Creates a file when given the meta data and uploadfile object, Inserts itself
        into the database, and saves the file in the shared volume
        """

        instance = cls(
            filename=meta.filename,
            tags=meta.tags
        )

        # Insert self into database
        instance.insert()

        # Write file into file system
        new_file = cls.__shared_volume__ / f"{instance.id}.base"
        with new_file.open("wb") as file_buffer:
            while chunk := await file.read(1024 * 1024):
                file_buffer.write(chunk)

        # Return self
        return instance

    @classmethod
    def gen_test(cls) -> list[tuple[Any, ImagesPostData]]:
        """
        Generates a random test file and meta data for said file
        Shouldn't be used in production since data used is purely random.

        :returns list: First item is the file data, second is meta data
        """
        
        def random_image():
            resp = requests.get("https://picsum.photos/1080/1920")
            if resp.status_code != 200:
                return requests.get("https://fastly.picsum.photos/id/508/1080/1920.jpg?hmac=Yr0rFxoJYNNuhneKtCVWGiR8gR_3Z3n847N7AHgoERE").content
            return resp.content
        
        file_name = f"image_{secrets.token_hex(4)}.png"

        file_data = ("files", (file_name, io.BytesIO(random_image()), "image/png"))
        meta_data = {"filename": file_name}

        return [file_data, meta_data]
