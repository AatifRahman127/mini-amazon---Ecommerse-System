"""
User management module
"""

import hashlib
from storage import Storage

def hash_password(raw_password):
    return hashlib.sha256(raw_password.encode()).hexdigest()

class UserManager:
    def __init__(self):
        self.storage = Storage("users.json")
        self.users = self.storage.load() or []
    
    def register(self):
        print("\n--- REGISTER ---")
        new_username = input("Username: ").strip()
        new_password = input("Password: ").strip()
        
        if not new_username:
            print("Username cannot be empty!")
            return False
        
        if len(new_password) < 6:
            print("Password must be at least 6 characters!")
            return False
        
        for account in self.users:
            if account["username"] == new_username:
                print("Username already exists!")
                return False
        
        self.users.append({"username": new_username, "password": hash_password(new_password)})
        self.storage.save(self.users)
        print("Registration successful!")
        return True
    
    def login(self):
        print("\n--- LOGIN ---")
        entered_username = input("Username: ").strip()
        entered_password = input("Password: ").strip()
        
        for account in self.users:
            if account["username"] == entered_username and account["password"] == hash_password(entered_password):
                print(f"Welcome back, {entered_username}!")
                return entered_username
        
        print("Invalid username or password!")
        return None
