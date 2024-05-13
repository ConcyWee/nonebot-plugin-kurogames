from pydantic import BaseModel
from pathlib import Path

class Config(BaseModel):
    KURO_DB_PATH = Path() / "data" / "kurogames"