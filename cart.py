"""
Shopping cart module
"""

from storage import Storage

class Cart:
    def __init__(self, username):
        self.username = username
        self.storage = Storage(f"cart_{username}.json")
        self.items = self.storage.load() or []
    
    def add_item(self, product_catalog):
        selected_id = input("\nProduct ID: ").strip().upper()
        selected_product = product_catalog.get_product(selected_id)
        
        if not selected_product:
            print("Product not found!")
            return
        
        try:
            desired_qty = int(input("Quantity: "))
            if desired_qty <= 0:
                print("Quantity must be positive!")
                return
            if desired_qty > selected_product['stock']:
                print(f"Only {selected_product['stock']} available!")
                return
        except ValueError:
            print("Invalid quantity!")
            return
        
        for cart_item in self.items:
            if cart_item['product_id'] == selected_id:
                cart_item['quantity'] += desired_qty
                self.storage.save(self.items)
                print(f"Updated {selected_product['name']} quantity!")
                return
        
        self.items.append({
            'product_id': selected_id,
            'name': selected_product['name'],
            'price': selected_product['price'],
            'quantity': desired_qty
        })
        self.storage.save(self.items)
        print(f"Added {selected_product['name']} to cart!")
    
    def remove_item(self):
        if not self.items:
            print("\nCart is empty!")
            return
        
        self.view()
        remove_id = input("\nProduct ID to remove: ").strip().upper()
        
        self.items = [cart_item for cart_item in self.items if cart_item['product_id'] != remove_id]
        self.storage.save(self.items)
        print("Item removed!")
    
    def view(self):
        if not self.items:
            print("\nYour cart is empty!")
            return
        
        print("\n" + "="*60)
        print("YOUR CART")
        print("="*60)
        cart_total = 0
        for cart_item in self.items:
            item_subtotal = cart_item['price'] * cart_item['quantity']
            cart_total += item_subtotal
            print(f"{cart_item['product_id']} | {cart_item['name']:<25} | {cart_item['quantity']} x ${cart_item['price']:.2f} = ${item_subtotal:.2f}")
        print("-"*60)
        print(f"TOTAL: ${cart_total:.2f}")
        print("="*60)
    
    def get_total(self):
        return sum(cart_item['price'] * cart_item['quantity'] for cart_item in self.items)
    
    def clear(self):
        self.items = []
        self.storage.save(self.items)