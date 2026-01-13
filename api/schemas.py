from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Transaction(BaseModel):
    id: Optional[int] = None
    body: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    type: Optional[str] = None

class Analytics(BaseModel):
    total_transactions: int
    total_amount: float

