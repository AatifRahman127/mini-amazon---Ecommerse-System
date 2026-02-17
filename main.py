
"""Mini-Amazon Console Application"""


from users import UserManager
from products import ProductCatalog
from cart import Cart
from orders import OrderManager

def main():
    user_manager = UserManager()
    product_catalog = ProductCatalog()
    order_manager = OrderManager()
    
    logged_in_user = None
    active_cart = None
    
    print("\n" + "="*40)
    print("  WELCOME TO MINI-AMAZON")
    print("="*40)
    
    while True:
        if not logged_in_user:
            print("\n1. Register")
            print("2. Login")
            print("3. Exit")
            menu_choice = input("\nChoice: ").strip()
            
            if menu_choice == "1":
                user_manager.register()
            
            elif menu_choice == "2":
                logged_in_user = user_manager.login()
                if logged_in_user:
                    active_cart = Cart(logged_in_user)
            
            elif menu_choice == "3":
                print("\nGoodbye!")
                break
            
            else:
                print("Invalid choice!")
        
        else:
            print(f"\n--- HELLO, {logged_in_user.upper()} ---")
            print("1. Browse products")
            print("2. Search products")
            print("3. View cart")
            print("4. Add to cart")
            print("5. Remove from cart")
            print("6. Checkout")
            print("7. Order history")
            print("8. Add new product (Admin)")
            print("9. Logout")
            store_choice = input("\nChoice: ").strip()
            
            if store_choice == "1":
                product_catalog.browse()
            
            elif store_choice == "2":
                product_catalog.search()
            
            elif store_choice == "3":
                active_cart.view()
            
            elif store_choice == "4":
                active_cart.add_item(product_catalog)
            
            elif store_choice == "5":
                active_cart.remove_item()
            
            elif store_choice == "6":
                order_manager.checkout(logged_in_user, active_cart, product_catalog)
            
            elif store_choice == "7":
                order_manager.view_history(logged_in_user)
            
            elif store_choice == "8":
                product_catalog.add_product()
            
            elif store_choice == "9":
                print(f"\nGoodbye, {logged_in_user}!")
                logged_in_user = None
                active_cart = None
            
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    main()