import re
from typing_effects import typingEffect


def create_user(user, password, email):
    if not user or not password or not email:
        raise UserCreationError(typingEffect("Failed to create a new user. Fill all the blanks!"))
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise UserCreationError(typingEffect("Failed to create with the provided email. Invalid email format."))

    return typingEffect("Successfully created user!")

    pass