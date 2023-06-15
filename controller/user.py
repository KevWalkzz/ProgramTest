class User:
    user = ""
    password = ""
    email = ""

    def __init__(self, email, user,password):
        self.email = email
        self.user = user
        self.password = password

    def get_user(self):
        return self.user
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
