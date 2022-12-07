from datetime import date
from typing import Optional

from pydantic import BaseModel


class Currency(BaseModel):
    code: str
    date: Optional[date]
    nominal: int
    value: float

    class Config:
        orm_mode = True
