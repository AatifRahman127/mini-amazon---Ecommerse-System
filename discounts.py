"""
Discount codes module
"""

from storage import Storage

class DiscountManager:
    def __init__(self):
        self.storage = Storage("discounts.json")
        self.discounts = self.storage.load()

        if not self.discounts:
            self.discounts = [
                {"code": "SAVE10", "type": "percentage", "value": 10},
                {"code": "SAVE20", "type": "percentage", "value": 20},
                {"code": "FLAT5", "type": "fixed", "value": 5},
                {"code": "FLAT15", "type": "fixed", "value": 15},
            ]
            self.storage.save(self.discounts)

    def apply_discount(self, cart_total):
        discount_code = input("\nEnter discount code (or press Enter to skip): ").strip().upper()

        if not discount_code:
            return cart_total, 0

        for discount in self.discounts:
            if discount["code"] == discount_code:
                if discount["type"] == "percentage":
                    discount_amount = cart_total * (discount["value"] / 100)
                else:
                    discount_amount = discount["value"]

                discount_amount = min(discount_amount, cart_total)
                final_total = cart_total - discount_amount

                print(f"Discount applied! You saved ${discount_amount:.2f}")
                return final_total, discount_amount

        print("Invalid discount code!")
        return cart_total, 0
