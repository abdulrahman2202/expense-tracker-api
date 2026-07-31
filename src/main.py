from fastapi import FastAPI

app = FastAPI(
    title="Smart Expense Tracker API",
    description="REST API for managing personal expenses",
    version="1.0.0"
)

@app.get("/")
def home():
    return{"message": "Welcome to the Smart Expense Tracker API"}