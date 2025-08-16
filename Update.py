def Update(productname, qn, filename):
    # Load existing inventory from the JSON file
    with open(filename, 'r') as file:
        data = json.load(file)  # data is a list of product dicts

    updated = False  # Flag to check if any product was updated

    # Iterate through the products
    for product in data:
        if product.get("name") == productname:
            new_quantity = product.get("quantity", 0) - int(qn)
            if new_quantity < 0:
                print(f"Warning: Quantity for {productname} cannot be negative. Setting to 0.")
                new_quantity = 0
            product["quantity"] = new_quantity
            updated = True
            print("Product Quantity Updated Successfully")

    if not updated:
        print(f"Product '{productname}' not found in inventory.")

    # Write updated data back to the JSON file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    # Example usage:
    print(f"Inventory After Selling the Respected Product: {productname}")