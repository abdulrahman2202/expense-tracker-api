from fastapi import APIRouter, status

from src.models.expense_model import ExpenseCreate
from src.services.expense_service import create_expense

from typing import Optional

from fastapi import Query

from src.services.expense_service import (
    create_expense,
    get_expenses
)

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.post("/",status_code=status.HTTP_201_CREATED)
def add_expense(expense: ExpenseCreate):
    """
    Add a new expense.
    """
    return create_expense(expense)


@router.get("/")
def get_all_expenses(
    category: Optional[str] = Query(
        default=None,
        description="Filter expenses by category"
    )
):
    return get_expenses(category)