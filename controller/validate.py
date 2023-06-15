import re

def validate_user(user=""):
    if len(user) >= 3:
        return True

    return False

def validate_password(password=""):
    if len(password) >= 3:
        return True

    return False

def validate_email(self, email=""):
    print(email)
    if len(email) >= 8:
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        
    return False