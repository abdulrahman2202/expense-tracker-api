from fastapi import APIRouter, status

from src.models.expense_model import ExpenseCreate
from src.services.expense_service import create_expense

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