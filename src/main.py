from inventory import Inventory
from category_manager import CategoryManager
from product_manager import ProductManager
from tabulate import tabulate
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def main():
    # Initialize managers
    inventory = Inventory()
    category_manager = CategoryManager()
    product_manager = ProductManager()

    while True:
        print(Fore.CYAN + "\n=== Inventory Management System ===" + Style.RESET_ALL)
        print(Fore.YELLOW + "1. View Categories")
        print("2. Add Category")
        print("3. View Products")
        print("4. Add Product")
        print("5. Update Stock (Add/Remove)")
        print("6. Sell Product")
        print("7. View Transaction History")
        print("8. Exit" + Style.RESET_ALL)

        choice = input(Fore.GREEN + "Enter your choice: " + Style.RESET_ALL)

        if choice == '1':
            categories = category_manager.get_all_categories()
            if not categories:
                print(Fore.RED + "No categories available." + Style.RESET_ALL)
            else:
                table = [[c['id'], c['name']] for c in categories]
                print(Fore.MAGENTA + tabulate(table, headers=["ID", "Name"], tablefmt="fancy_grid") + Style.RESET_ALL)

        elif choice == '2':
            name = input("Enter new category name: ")
            category_manager.add_category(name)
            print(Fore.GREEN + f"Category '{name}' added successfully!" + Style.RESET_ALL)

        elif choice == '3':
            products = inventory.view_inventory()
            if not products:
                print(Fore.RED + "No products available." + Style.RESET_ALL)
            else:
                table = [[p['id'], p['name'], p['category_name'], p['price'], p['stock']] for p in products]
                print(Fore.BLUE + tabulate(table, headers=["ID", "Name", "Category", "Price", "Stock"], tablefmt="fancy_grid") + Style.RESET_ALL)

        elif choice == '4':
            name = input("Enter product name: ")
            category_id = input("Enter category ID: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter initial stock quantity: "))
            product_manager.add_product(name, category_id, price, stock)
            print(Fore.GREEN + f"Product '{name}' added successfully!" + Style.RESET_ALL)

        elif choice == '5':
            product_id = input("Enter product ID: ")
            action = input("Type 'add' to add stock or 'remove' to remove stock: ").lower()
            quantity = int(input("Enter quantity: "))
            if action == 'add':
                inventory.add_stock(product_id, quantity)
            elif action == 'remove':
                inventory.remove_stock(product_id, quantity)
            else:
                print(Fore.RED + "Invalid action." + Style.RESET_ALL)

        elif choice == '6':
            product_id = input("Enter product ID to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            inventory.remove_stock(product_id, quantity)

        elif choice == '7':
            transactions = inventory.view_transactions()
            if not transactions:
                print(Fore.RED + "No transactions found." + Style.RESET_ALL)
            else:
                table = [[t['id'], t['product_name'], t['quantity'], t['type'], t['date']] for t in transactions]
                print(Fore.CYAN + tabulate(table, headers=["ID", "Product", "Quantity", "Type", "Date"], tablefmt="fancy_grid") + Style.RESET_ALL)

        elif choice == '8':
            print(Fore.YELLOW + "Exiting IMS. Goodbye!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
