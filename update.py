# Inventory Update Function
def UpdateJSON(productname, qn, filename):
    """
    Updates inventory stored in a JSON file.
    
    :param productname: Name of the product to update
    :param qn: Quantity sold
    :param filename: Path to JSON inventory file
    """
    # Load data from JSON file
    with open(filename, 'r') as file:
        data = json.load(file)  # Data is a list of dictionaries

    updated = False  # To track if we actually updated something

    for product in data:
        if product.get("name") == productname:
            new_quantity = product.get("quantity", 0) - int(qn)

            if new_quantity < 0:
                print(f"Warning: Quantity for {productname} cannot be negative. Setting to 0.")
                new_quantity = 0

            product["quantity"] = new_quantity
            updated = True
            print("Product Quantity Updated Successfully")

    # Write updated data back to JSON file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    if not updated:
        print(f"Product '{productname}' not found in inventory.")