# Manage category operations

import json
import os
import utils as ut  # Assumed to include: load_json, write_json, get_data_directory

# Constants
CATEGORY_FILE = 'categories.json'  # File name to store categories
DATA = os.path.join(ut.get_data_directory(), CATEGORY_FILE)  # Full path to the category file


def get_all_categories():
    """
    Loads and returns all categories from the JSON file.

    Returns:
        list: List of category dictionaries. Returns an empty list if loading fails.
    """
    try:
        categories = ut.load_json(DATA)  # Load data using utility function
        if not isinstance(categories, list):
            raise ValueError("Categories data should be a list.")
        return categories
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        # Handle cases: file not found, JSON format error, or wrong data structure
        print(f"Error loading categories: {e}")
        return []  # Return empty list on error


def find_category_by_id(category_id):
    """
    Finds and returns a category by its ID.

    Args:
        category_id (str): The ID of the category to find.

    Returns:
        dict or None: The matching category dictionary if found, otherwise None.
    """
    categories = get_all_categories()  # Load all categories
    for category in categories:
        if category.get('id') == category_id:
            return category
    return None  # Return None if not found


def update_categories(categories):
    """
    Writes the given list of categories to the JSON file.

    Args:
        categories (list): List of category dictionaries to save.
    """
    try:
        ut.write_json(DATA, categories)  # Write updated categories to file
    except (TypeError, OSError) as e:
        print(f"Error writing categories: {e}")  # Handle write errors


def add_category(new_category):
    """
    Adds a new category to the list and updates the JSON file.

    Args:
        new_category (dict): The new category dictionary to add.

    Raises:
        TypeError: If new_category is not a dictionary.
    """
    if not isinstance(new_category, dict):
        raise TypeError("New category must be a dictionary.")

    categories = get_all_categories()
    categories.append(new_category)  # Add the new category
    update_categories(categories)  # Save back to JSON


def remove_category(category_id):
    """
    Removes a category from the list by its ID and updates the JSON file.

    Args:
        category_id (str): The ID of the category to remove.
    """
    categories = get_all_categories()
    # Keep all categories except the one with the matching ID
    updated_categories = [cat for cat in categories if cat.get('id') != category_id]
    update_categories(updated_categories)
