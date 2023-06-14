import re
from typing_effects import typingEffect, typingEffectInput

class UserCreationError(Exception):
    pass

def create_user(user, password, email):
    if not user or not password or not email:
        raise UserCreationError(typingEffect("Failed to create a new user. Fill all the blanks!"))
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise UserCreationError(typingEffect("Failed to create with the provided email. Invalid email format."))

    return typingEffect("Successfully created user!")


def get_user_credentials():
    username = typingEffectInput("What's your name? ").strip()
    password = typingEffectInput("Please, insert a password. ").strip()
    email = typingEffectInput("Please, insert a valid email. ").strip()
    return username, password, email


def handle_user_creation():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username, password, email = get_user_credentials()
        try:
            feedback = create_user(username, password, email)
            return username, password

        except UserCreationError as e:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            typingEffect(f"{remaining_attempts} attempts left.")

    typingEffect("Maximum attempts reached. Exiting program.")
    exit()
