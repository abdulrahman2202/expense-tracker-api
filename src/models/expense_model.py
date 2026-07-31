from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=1, max_length=50)
    date: date


class ExpenseResponse(BaseModel):
    id: UUID
    title: str
    amount: float
    category: str
    date: date

class SummaryResponse(BaseModel):
    category: str | None = None
    total: float

class MessageResponse(BaseModel):
    message: str