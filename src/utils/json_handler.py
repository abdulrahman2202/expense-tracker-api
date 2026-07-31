import json
import os

DEFAULT_FILE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "expenses.json"
)


def get_data_file():
    return os.getenv("EXPENSE_FILE", DEFAULT_FILE)


def load_expenses(file_path=None):
    file_path = file_path or get_data_file()

    with open(file_path, "r") as file:
        return json.load(file)


def save_expenses(expenses, file_path=None):
    file_path = file_path or get_data_file()

    with open(file_path, "w") as file:
        json.dump(expenses, file, indent=4)