import json
import os

# Path to the JSON file
DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "expenses.json"
)


def load_expenses():
    """
    Read all expenses from the JSON file.
    """
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    """
    Save all expenses to the JSON file.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)