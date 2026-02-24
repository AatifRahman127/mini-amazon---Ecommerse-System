"""
Product catalog module
"""

from storage import Storage

class ProductCatalog:
    def __init__(self):
        self.storage = Storage("products.json")
        self.products = self.storage.load()
        
        if not self.products:
            self.products = [
                {"product_id": "P1001", "name": "USB-C Cable", "price": 9.99, "stock": 30},
                {"product_id": "P1002", "name": "Wireless Mouse", "price": 19.99, "stock": 15},
                {"product_id": "P1003", "name": "Bluetooth Keyboard", "price": 49.99, "stock": 10},
                {"product_id": "P1004", "name": "Laptop Stand", "price": 29.99, "stock": 20},
                {"product_id": "P1005", "name": "Webcam HD", "price": 59.99, "stock": 8},
            ]
            self.storage.save(self.products)
    
    def browse(self):
        print("\n" + "="*60)
        print("PRODUCT CATALOG")
        print("="*60)
        for item in self.products:
            print(f"{item['product_id']} | {item['name']:<25} | ${item['price']:<7.2f} | Stock: {item['stock']}")
        print("="*60)
    
    def search(self):
        search_term = input("\nSearch keyword: ").strip().lower()
        matches = [item for item in self.products if search_term in item['name'].lower()]
        
        if matches:
            print("\n" + "="*60)
            for item in matches:
                print(f"{item['product_id']} | {item['name']:<25} | ${item['price']:<7.2f} | Stock: {item['stock']}")
            print("="*60)
        else:
            print("No products found!")
    
    def get_product(self, prod_id):
        for item in self.products:
            if item['product_id'] == prod_id:
                return item
        return None
    
    def update_stock(self, prod_id, amount_change):
        for item in self.products:
            if item['product_id'] == prod_id:
                item['stock'] += amount_change
                self.storage.save(self.products)
                return True
        return False
    
    def add_product(self):
        print("\n--- ADD NEW PRODUCT ---")
        new_id = input("Product ID (e.g., P1006): ").strip().upper()
        
        if self.get_product(new_id):
            print("Product ID already exists!")
            return
        
        product_name = input("Product name: ").strip()
        try:
            product_price = float(input("Price: $"))
            available_stock = int(input("Stock quantity: "))
            
            if product_price <= 0 or available_stock < 0:
                print("Invalid price or stock!")
                return
        except ValueError:
            print("Invalid input!")
            return
        
        self.products.append({
            "product_id": new_id,
            "name": product_name,
            "price": product_price,
            "stock": available_stock
        })
        self.storage.save(self.products)
        print(f"Product '{product_name}' added successfully!")
