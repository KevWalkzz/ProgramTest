import re
from typing_effects import typingEffect, typingEffectInput

class User:
    user = ""
    password = ""
    email = ""

    def __init__(self):
        pass

    def validate_user(self, user=""):
        if len(user) >= 3:
            self.user = user
            return True
        
        return False
    
    def validate_password(self, password=""):
        if len(password) >= 3:
            self.password = password
            return True
        
        return False

    def validate_email(self, email=""):
        if len(email) >= 8:
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return True
            
        return False
    
    def get_user(self):
        return self.user
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
