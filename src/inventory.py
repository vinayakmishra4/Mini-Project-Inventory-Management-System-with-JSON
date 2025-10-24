# importing utility functions
import utils as ut
# this module handles the product inventory management
import product_manager as pd
# importing transaction manager for handling transactions
import transaction_manager as tm

class Inventory:
    def __init__(self, product_file='data/products.json', transaction_file='data/transactions.json'):
        self.product_manager = pd.ProductManager(product_file)
        self.transaction_manager = tm.TransactionManager(transaction_file)

    def check_stock(self, product_id, quantity):
        product = self.product_manager.find_product_by_id(product_id)
        if not product:
            print("Product not found.")
            return False
        if product['stock_quantity'] >= quantity:
            return True
        else:
            print(f"Insufficient stock. Available: {product['stock_quantity']}")
            return False
        
    def add_stock(self, product_id, quantity):
        product = self.product_manager.find_product_by_id(product_id)
        if not product:
            print("Product not found.")
            return
        self.product_manager.update_stock(product_id, quantity)
        self.transaction_manager.log_transaction(product_id, "purchase", quantity)
        print(f"Added {quantity} units to {product['name']}.")

    def remove_stock(self, product_id, quantity):
        if not self.check_stock(product_id, quantity):
            return
        self.product_manager.update_stock(product_id, -quantity)
        self.transaction_manager.log_transaction(product_id, "sale", quantity)
        product = self.product_manager.find_product_by_id(product_id)
        print(f"Sold {quantity} units of {product['name']}.")
    
    def view_inventory(self):
        products = self.product_manager.get_all_products()
        if not products:
            print("No products in inventory.")
            return
        print("Current Inventory:")
        print("ID | Name | Category ID | Price | Stock")
        for p in products:
            print(f"{p['id']} | {p['name']} | {p['category_id']} | {p['price']} | {p['stock_quantity']}")
        
    def view_transactions(self):
        transactions = self.transaction_manager.get_all_transactions()
        if not transactions:
            print("No transactions recorded.")
            return
        print("Transaction History:")
        print("Product ID | Type | Quantity | Timestamp")
        for t in transactions:
            print(f"{t['product_id']} | {t['type']} | {t['quantity']} | {t['timestamp']}")





