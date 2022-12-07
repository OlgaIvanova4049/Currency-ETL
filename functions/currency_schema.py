from datetime import date
from typing import Optional

from pydantic import BaseModel


class CurrencySchema(BaseModel):
    code: str
    nominal: int
    value: float
    date: Optional[date]
