from fastapi import APIRouter, Query, status
from typing import Optional

from src.models.expense_model import (
    ExpenseCreate,
    ExpenseResponse,
    SummaryResponse,
    MessageResponse
)
from src.services.expense_service import (
    create_expense,
    get_expenses,
    get_summary,
    delete_expense,
)

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)



@router.post(
    "/",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new expense",
    description="Create a new expense and store it in the JSON file."
)
def add_expense(expense: ExpenseCreate):
    return create_expense(expense)


@router.get(
    "/",
    response_model=list[ExpenseResponse],
    summary="Get all expenses",
    description="Returns all expenses. Optionally filter by category using the category query parameter."
)
def get_all_expenses(
    category: Optional[str] = Query(
        default=None,
        description="Filter expenses by category"
    )
):
    return get_expenses(category)

@router.get(
    "/summary",
    response_model=SummaryResponse,
    response_model_exclude_none=True,
    summary="Calculate expense summary",
    description="Returns the total expenses overall or for a specific category."
)
def summary(
    category: Optional[str] = Query(
        default=None,
        description="Filter summary by category"
    )
):
    return get_summary(category)


@router.delete(
    "/{expense_id}",
    response_model=MessageResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete an expense",
    description="Delete an expense using its unique ID."
)
def delete(expense_id: str):
    return delete_expense(expense_id)