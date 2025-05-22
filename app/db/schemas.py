# schemas.py
from pydantic import BaseModel

class Face(BaseModel):
    id: int
    name: str
    image_path: str | None

    class Config:
        orm_mode = True