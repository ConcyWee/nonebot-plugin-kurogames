from pydantic import BaseModel
from pathlib import Path

class Config(BaseModel):
    kuro_db_path : str= str(Path() / "data" / "kurogames") #数据库路径，放置用户使用字符串，先强转为str，调用时再转为Path