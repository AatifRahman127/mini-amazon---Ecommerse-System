# mini-amazon---Ecommerse-System
Console-based e-commerce system built with Python

## How to Run

1. Make sure Python 3 is installed on your system
2. Place all files in the same folder
3. Open terminal in that folder and run:
```
python main.py
```

---

## Files

| File | Purpose |
|------|---------|
| `main.py` | 
| `users.py` | 
| `products.py` | 
| `cart.py` | 
| `orders.py` | 
| `discounts.py` | 
| `storage.py` | 

---

## Features

 1. User System
 2. Product Catalog
 3. Shopping Cart
 4. Checkout
 5. Order History
 6. Add New Product (Admin)


---

## Discount Codes

Apply these codes at checkout for a discount:

| Code | Type | Discount |
|------|------|----------|
| `SAVE10` | Percentage | 10% off |
| `SAVE20` | Percentage | 20% off |
| `FLAT5` | Fixed | $5 off |
| `FLAT15` | Fixed | $15 off |

- Discounts cannot exceed the cart total
- Press Enter at the discount prompt to skip

---

## Sample Products

These products are loaded automatically on first run:

| ID | Name | Price | Stock |
|----|------|-------|-------|
| P1001 | USB-C Cable | $9.99 | 30 |
| P1002 | Wireless Mouse | $19.99 | 15 |
| P1003 | Bluetooth Keyboard | $49.99 | 10 |
| P1004 | Laptop Stand | $29.99 | 20 |
| P1005 | Webcam HD | $59.99 | 8 |

---

## Data Storage

All data is automatically saved to JSON files in the project folder:
Data persists between sessions meaning all your users, products, carts and orders will still be there when you restart the program.
---

## Known Limitations

- No proper admin system, any user with admin command can add products
- Discount codes cannot be added through the program, only by editing `discounts.json`
- No product categories or filters beyond keyword search
