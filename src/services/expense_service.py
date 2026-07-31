from uuid import uuid4
from fastapi import HTTPException

from src.models.expense_model import ExpenseCreate
from src.utils.json_handler import load_expenses, save_expenses


def create_expense(expense: ExpenseCreate):
    """
    Create a new expense and save it to the JSON file.
    """

    # Read existing expenses
    expenses = load_expenses()

    # Create new expense dictionary
    new_expense = {
        "id": str(uuid4()),
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "date": str(expense.date)
    }

    # Add to list
    expenses.append(new_expense)

    # Save back to JSON
    save_expenses(expenses)

    return new_expense


def get_expenses(category: str = None):
    """
    Get all expenses.
    If category is provided, return only matching expenses.
    """

    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return expenses


def get_summary(category: str = None):

    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

        return {
            "category": category,
            "total": sum(expense["amount"] for expense in expenses)
        }

    return {
        "total": sum(expense["amount"] for expense in expenses)
    }

    

def delete_expense(expense_id: str):
    """
    Delete an expense by ID.
    """

    expenses = load_expenses()

    for expense in expenses:

        if expense["id"] == expense_id:

            expenses.remove(expense)

            save_expenses(expenses)

            return {
                "message": "Expense deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )


def search_expenses(query: str):
    """
    Search expenses by title or category.
    """

    expenses = load_expenses()

    query = query.lower()

    results = [
        expense
        for expense in expenses
        if query in expense["title"].lower()
        or query in expense["category"].lower()
    ]

    return results