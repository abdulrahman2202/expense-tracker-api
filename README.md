# 💰 Smart Expense Tracker API

A RESTful Expense Tracker API built with **FastAPI** that allows users to manage personal expenses. This project was developed as part of the **Software Engineering Apprenticeship Assignment 2026**.

![Python](https://img.shields.io/badge/Python-3.12-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.141.1-green) ![Pytest](https://img.shields.io/badge/Tests-10%20Passed-success)


## Project Information

- **Author:** Abdul Rahman
- **Language:** Python 3.12
- **Framework:** FastAPI
- **Storage:** JSON File
- **API Documentation:** Swagger (OpenAPI)
- **Testing:** Pytest
- **Version:** 1.0.0

---

## 🚀 Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Search expenses by title or category *(Optional Bonus Feature)*
- Delete an expense
- Automatic request validation using Pydantic
- Interactive API documentation with Swagger (OpenAPI)
- Local JSON file storage (No database required)
- Automated tests using Pytest

---

## 🛠️ Tech Stack

- Python 3.12+
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- JSON File Storage

---

## 📁 Project Structure

```text
expense-tracker-api/
│
├── src/
│   ├── main.py
│   ├── data/
│   ├── models/
│   ├── routers/
│   ├── services/
│   └── utils/
│
├── tests/
│   ├── conftest.py
│   ├── test_expense.py
│   └── test_expenses.json
│
├── README.md
├── AI_NOTES.md
├── LICENSE
├── requirements.txt
├── pytest.ini
└── .gitignore
```
---
## Prerequisites

Before running this project, ensure you have:

- Python 3.12 or later
- Git
- pip

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/abdulrahman2202/expense-tracker-api.git
```

## 2. Move into the project

```bash
cd expense-tracker-api
```

## 3. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

Command Prompt

```bash
venv\Scripts\activate
```

PowerShell

```powershell
venv\Scripts\Activate.ps1
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Development Server

```bash
uvicorn src.main:app --reload
```

The API will start at:

```
http://127.0.0.1:8000
```


---

# 📖 Swagger Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🧪 Run Tests

```bash
pytest -v
```

Expected

```
10 passed
```

---

# 📌 API Endpoints

## Create Expense

```
POST /expenses/
```

Example Request

```json
{
    "title": "Pizza",
    "amount": 300,
    "category": "Food",
    "date": "2026-08-01"
}
```

---

## Get All Expenses

```
GET /expenses/
```

---

## Filter Expenses

```
GET /expenses/?category=Food
```

---

## Expense Summary

Overall

```
GET /expenses/summary
```

Category

```
GET /expenses/summary?category=Food
```

---

## Search Expenses

```
GET /expenses/search?q=Pizza
```
Searches expenses by **title** or **category**.

---

## Delete Expense

```
DELETE /expenses/{expense_id}
```

---

# ✅ Validation

The API automatically validates:

- Title cannot be empty
- Category cannot be empty
- Amount must be greater than zero
- Date must be a valid date

---

# 📊 Testing

The project contains automated tests using **Pytest**.

The automated test suite covers:

- Home endpoint
- Create expense
- Retrieve all expenses
- Filter expenses by category
- Expense summary
- Category summary
- Search expenses
- Invalid validation
- Delete expense
- Delete invalid expense

---

# 👨‍💻 Author

**Abdul Rahman**

- GitHub: https://github.com/abdulrahman2202
- LinkedIn: https://www.linkedin.com/in/abdul-rahman-001b34279/

Feel free to connect with me for discussions about Python, FastAPI, Backend Development, and Software Engineering.


---

# 📝 License

This project is licensed under the MIT License.

