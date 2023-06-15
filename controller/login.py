import user

class AttemptsError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Erro: {}".format(self.message)

class Login(user.User):
    login_max_attempts = 3

    def login(self, user, email, password):
        self.login_max_attempts -= 1

        if self.get_user() == user and self.get_email() == email and self.get_password() == password:
            return True

        if self.login_max_attempts == 0:
           raise AttemptsError("maximum number of attempts reached") 

        return False
    