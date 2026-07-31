from fastapi import FastAPI

from src.routers.expense_router import router as expense_router

app = FastAPI(
    title="Smart Expense Tracker API",
    description="""
A REST API built with FastAPI for managing personal expenses.

## Features

- Add Expense
- View Expenses
- Filter by Category
- Expense Summary
- Delete Expense

Created for the Software Engineering Apprenticeship Assignment.
""",
    version="1.0.0",
    contact={
        "name": "Abdul Rahman",
        "email": "abdulrahman2.ar@gmail.com"
    }
)

app.include_router(expense_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Expense Tracker API"
    }