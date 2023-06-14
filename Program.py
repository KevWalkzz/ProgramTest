from calculator import *
from user import create_user
from typing_effects import typingEffect, typingEffectInput


def get_user_credentials():
    username = typingEffectInput("What's your name? ").strip()
    password = typingEffectInput("Please, insert a password. ").strip()
    email = typingEffectInput("Please, insert a valid email. ").strip()
    return username, password, email


def handle_user_creation():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        try:
            username, password, email = get_user_credentials()
            feedback = create_user(username, password, email)
            return username, password

        except UserCreationError as e:
            print(str(e))
            attempts += 1

    if attempts == max_attempts:
        typingEffect("Maximum attempts reached. Exiting program.")
        exit()


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
            typingEffect(
                f"{conf} is not your password! You have {remaining_attempts} attempts left.")

    typingEffect("Maximum attempts reached. Exiting program.")
    exit()


def main():
    username, password = handle_user_creation()
    password_confirmation(password, username)

    selection = typingEffectInput(f"What do you want today, {username}? Options: Calculator. ").capitalize()

    if selection == "Calculator":
        calculator(username)
    else:
        typingEffect("That's not a valid option!")


if __name__ == "__main__":
    main()
