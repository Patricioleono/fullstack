from pydantic import BaseModel
from typing import Optional

class newCatInsert(BaseModel):
    id:      Optional[int]
    catName: str
    catRace: str
    catYear: int
    catImg:  str