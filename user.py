import re
from sys import exit
from typing_effects import typingEffect, typingEffectInput

class User:
    user = ""
    password = ""
    email = ""
    login_max_attempts = 3

    def __init__(self):
        pass

    def login(self, user, email, password):
        self.login_max_attempts -= 1

        if self.user == user and self.email == email and self.password == password:
            return True
        
        if self.login_max_attempts == 0:
            typingEffect("maximum number of attempts reached")
            exit()
        
        return False

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
                self.email = email
                return True
            
        return False
    
    def get_user(self):
        return self.user
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
