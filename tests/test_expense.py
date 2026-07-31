from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def create_sample_expense():
    """
    Helper function to create a sample expense.
    """

    expense = {
        "title": "Pizza",
        "amount": 300,
        "category": "Food",
        "date": "2026-08-01"
    }

    return client.post("/expenses/", json=expense)


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["message"] == "Welcome to Smart Expense Tracker API"


def test_create_expense():

    response = create_sample_expense()

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert data["title"] == "Pizza"
    assert data["amount"] == 300
    assert data["category"] == "Food"


def test_get_all_expenses():

    create_sample_expense()

    response = client.get("/expenses/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    assert len(data) == 1


def test_filter_by_category():

    create_sample_expense()

    response = client.get("/expenses/?category=Food")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1

    assert data[0]["category"] == "Food"


def test_summary():

    create_sample_expense()

    response = client.get("/expenses/summary")

    assert response.status_code == 200

    data = response.json()

    assert data["total"] == 300


def test_summary_by_category():

    create_sample_expense()

    response = client.get("/expenses/summary?category=Food")

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "Food"

    assert data["total"] == 300


def test_search():

    create_sample_expense()

    response = client.get(
        "/expenses/search?q=Pizza"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1

    assert data[0]["title"] == "Pizza"


def test_invalid_amount():

    expense = {
        "title": "Pizza",
        "amount": -100,
        "category": "Food",
        "date": "2026-08-01"
    }

    response = client.post(
        "/expenses/",
        json=expense
    )

    assert response.status_code == 422


def test_delete_expense():

    create = create_sample_expense()

    expense_id = create.json()["id"]

    response = client.delete(
        f"/expenses/{expense_id}"
    )

    assert response.status_code == 200

    assert response.json()["message"] == "Expense deleted successfully"


def test_delete_invalid_expense():

    response = client.delete(
        "/expenses/123456"
    )

    assert response.status_code == 404