import json
import uuid
from datetime import datetime
from .utils import read_json, write_json
import os

# Optional: dynamically read from config.json later
TRANSACTIONS_FILE = os.path.join(os.path.dirname(__file__), '../data/transactions.json')


def get_all_transactions():
    """Return all transactions as a list."""
    return read_json(TRANSACTIONS_FILE)


def log_transaction(product_id, type, quantity):
    """Log a new transaction entry."""
    transactions = read_json(TRANSACTIONS_FILE)

    new_transaction = {
        "id": str(uuid.uuid4()),
        "product_id": product_id,
        "type": type,  # e.g., "sale" or "restock"
        "quantity": quantity,
        "timestamp": datetime.now().isoformat()
    }

    transactions.append(new_transaction)
    write_json(TRANSACTIONS_FILE, transactions)
    return new_transaction


def find_transaction_by_id(transaction_id):
    """Find a transaction by its unique ID."""
    transactions = read_json(TRANSACTIONS_FILE)
    for t in transactions:
        if t["id"] == transaction_id:
            return t
    return None


def get_transactions_by_product(product_id):
    """Get all transactions related to a specific product."""
    transactions = read_json(TRANSACTIONS_FILE)
    return [t for t in transactions if t["product_id"] == product_id]


def get_transactions_by_type(type):
    """Get transactions filtered by type (e.g., sale or restock)."""
    transactions = read_json(TRANSACTIONS_FILE)
    return [t for t in transactions if t["type"].lower() == type.lower()]
