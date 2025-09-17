"""
Inventory Management System package.

This package provides modules for managing products, categories,
transactions, and inventory using JSON as storage.
"""

from . import inventory
from . import utils
from . import product_manager
from . import category_manager
from . import transaction_manager

__version__ = "0.1.0"

__all__ = [
    "inventory",
    "utils",
    "product_manager",
    "category_manager",
    "transaction_manager",
]
