"""
Storage module - Handles file I/O operations
"""

import json
import os

class Storage:
    def __init__(self, filename):
        self.filename = filename
        self.filepath = filename
    
    def load(self):
        try:
            if os.path.exists(self.filepath):
                with open(self.filepath, 'r') as file:
                    return json.load(file)
            return None
        except json.JSONDecodeError:
            print(f"Error: Could not read {self.filename}")
            return None
        except Exception as error:
            print(f"Error loading {self.filename}: {error}")
            return None
    
    def save(self, data):
        try:
            with open(self.filepath, 'w') as file:
                json.dump(data, file, indent=2)
            return True
        except Exception as error:
            print(f"Error saving {self.filename}: {error}")
            return False
    
    def delete(self):
        try:
            if os.path.exists(self.filepath):
                os.remove(self.filepath)
                return True
            return False
        except Exception as error:
            print(f"Error deleting {self.filename}: {error}")
            return False