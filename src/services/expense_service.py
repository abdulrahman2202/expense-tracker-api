from uuid import uuid4

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