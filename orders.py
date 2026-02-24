"""
Order management module
"""

from datetime import datetime
from storage import Storage
from discounts import DiscountManager

class OrderManager:
    def __init__(self):
        self.storage = Storage("orders.json")
        self.orders = self.storage.load() or []
        self.discount_manager = DiscountManager()

    def checkout(self, buyer_name, shopping_cart, product_catalog):
        if not shopping_cart.items:
            print("\nCart is empty!")
            return

        shopping_cart.view()
        user_confirmation = input("\nConfirm checkout? (y/n): ").lower()

        if user_confirmation != 'y':
            print("Checkout cancelled!")
            return

        for cart_item in shopping_cart.items:
            available_product = product_catalog.get_product(cart_item['product_id'])
            if not available_product or available_product['stock'] < cart_item['quantity']:
                print(f"Insufficient stock for {cart_item['name']}!")
                return

        original_total = shopping_cart.get_total()
        final_total, saved_amount = self.discount_manager.apply_discount(original_total)

        for cart_item in shopping_cart.items:
            product_catalog.update_stock(cart_item['product_id'], -cart_item['quantity'])

        new_order_id = f"O{len(self.orders) + 1:04d}"
        purchase_record = {
            'order_id': new_order_id,
            'username': buyer_name,
            'items': shopping_cart.items.copy(),
            'original_total': original_total,
            'discount': saved_amount,
            'total': final_total,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.orders.append(purchase_record)
        self.storage.save(self.orders)

        shopping_cart.clear()

        print("\n" + "="*60)
        print("ORDER RECEIPT")
        print("="*60)
        print(f"Order ID: {new_order_id}")
        print(f"Date: {purchase_record['timestamp']}")
        print("-"*60)
        for purchased_item in purchase_record['items']:
            print(f"{purchased_item['name']} x {purchased_item['quantity']} = ${purchased_item['price'] * purchased_item['quantity']:.2f}")
        print("-"*60)
        if saved_amount > 0:
            print(f"Subtotal:  ${original_total:.2f}")
            print(f"Discount:  -${saved_amount:.2f}")
        print(f"TOTAL:     ${final_total:.2f}")
        print("="*60)
        print("Thank you for your purchase!")

    def view_history(self, customer_name):
        customer_orders = [order_record for order_record in self.orders if order_record['username'] == customer_name]

        if not customer_orders:
            print("\nNo order history!")
            return

        print("\n" + "="*60)
        print("ORDER HISTORY")
        print("="*60)
        for order_record in customer_orders:
            print(f"Order {order_record['order_id']} | {order_record['timestamp']} | ${order_record['total']:.2f}")
        print("="*60)
