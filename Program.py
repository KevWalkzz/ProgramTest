from user import *
from calculator import calculator
from passconfirm import password_confirmation
from typing_effects import typingEffect, typingEffectInput


def main():
    username, password = handle_user_creation()
    password_confirmation(password, username)

    selection = typingEffectInput(f"What do you want today, {username}? Options: Calculator. ").capitalize()

    if selection == "Calculator":
        calculator()
    else:
        typingEffect("That's not a valid option!")


if __name__ == "__main__":
    main()
