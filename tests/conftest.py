import json
import os
import pytest

TEST_FILE = os.path.join(
    os.path.dirname(__file__),
    "test_expenses.json"
)

os.environ["EXPENSE_FILE"] = TEST_FILE


@pytest.fixture(autouse=True)
def clean_test_file():

    with open(TEST_FILE, "w") as file:
        json.dump([], file)

    yield

    with open(TEST_FILE, "w") as file:
        json.dump([], file)