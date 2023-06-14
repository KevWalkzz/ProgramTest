import user
from typing_effects import *

def password_confirmation(password, username):
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        conf = typingEffectInput("To log in, input your password. ")
        if conf == password:
            typingEffect(f"Welcome, {username}!")
            return
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            typingEffect(f"{conf} is not your password! You have {remaining_attempts} attempts left.")

    typingEffect("Maximum attempts reached. Exiting program.")
    exit()
