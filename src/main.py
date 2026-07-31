from fastapi import FastAPI

from src.routers.expense_router import router as expense_router

app = FastAPI(
    title="Smart Expense Tracker API",
    description="REST API for managing personal expenses",
    version="1.0.0"
)

app.include_router(expense_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Expense Tracker API"
    }