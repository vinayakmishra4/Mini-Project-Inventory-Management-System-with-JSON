import json
import os
from utils import read_json, write_json  # Utility functions to read/write JSON data
import uuid  # For generating unique product IDs

# Define the path to the JSON file that stores product data
PRODUCTS_FILE = os.path.join("data", "products.json")

# Function to retrieve all products from the JSON file
def get_all_products():
    return read_json(PRODUCTS_FILE)

# Function to find a specific product by its unique ID
def find_product_by_id(product_id):
    products = get_all_products()
    for product in products:
        if product["id"] == product_id:
            return product  # Return the matching product
    return None  # Return None if no product is found

# Function to add a new product to the JSON file
def add_product(name, category_id, price, stock_quantity):
    products = get_all_products()

    # Create a new product dictionary with a unique UUID
    new_product = {
        "id": str(uuid.uuid4()),  # Generate a unique string ID
        "name": name,
        "category_id": category_id,
        "price": price,
        "stock_quantity": stock_quantity
    }

    # Append the new product to the existing list
    products.append(new_product)

    # Write updated product list back to the JSON file
    write_json(PRODUCTS_FILE, products)

    # Return the newly created product
    return new_product

# Function to update the stock quantity of a product
def update_stock(product_id, quantity_change):
    products = get_all_products()
    updated = False

    for product in products:
        if product["id"] == product_id:
            # Calculate new stock quantity
            new_quantity = product["stock_quantity"] + quantity_change
            if new_quantity < 0:
                raise ValueError("Insufficient stock for this operation.")  # Prevent negative stock
            product["stock_quantity"] = new_quantity
            updated = True
            break

    if updated:
        write_json(PRODUCTS_FILE, products)  # Save changes
        return True
    else:
        return False  # Product ID not found

# Function to delete a product by ID
def delete_product(product_id):
    products = get_all_products()

    # Filter out the product to be deleted
    new_products = [p for p in products if p["id"] != product_id]

    # If no product was removed, return False
    if len(new_products) == len(products):
        return False

    # Save the updated list without the deleted product
    write_json(PRODUCTS_FILE, new_products)
    return True

# Function to update a product's details (name, category, price)
def update_product(product_id, name=None, category_id=None, price=None):
    products = get_all_products()
    updated = False

    for product in products:
        if product["id"] == product_id:
            # Update only the provided fields
            if name:
                product["name"] = name
            if category_id:
                product["category_id"] = category_id
            if price:
                product["price"] = price
            updated = True
            break

    if updated:
        write_json(PRODUCTS_FILE, products)  # Save changes
        return True
    else:
        return False  # Product not found or nothing to update
