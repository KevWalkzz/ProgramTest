import time
import re
import sqlite3
import sys
import gettext


class UserCreationError(Exception):
    pass


def typingEffect(text, speed=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()


def typingEffectInput(prompt, speed=0.05):
    input_text = ""
    for char in prompt:
        input_text += char
        print(char, end="", flush=True)
        time.sleep(speed)
    user_input = input()
    return user_input


def createUser(user, password, email):
    if not user or not password or not email:
        raise UserCreationError(typingEffect("Failed to create a new user. Fill all the blanks!"))
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise UserCreationError(typingEffect("Failed to create with the provided email. Invalid email format."))

    return typingEffect("Successfully created user!")


max_attempts = 3
attempts = 0

while attempts < max_attempts:
    try:
        # Account Inputs
        username = typingEffectInput("What's your name? ")
        password = typingEffectInput("Please, insert a password. ")
        email = typingEffectInput("Please, insert a valid email. ")

        # Remove whitespace from string
        username = username.strip()
        password = password.strip()
        email = email.strip()

        feedback = createUser(username, password, email)
        break

    except UserCreationError as e:
        print(str(e))
        attempts += 1

if attempts == max_attempts:
    typingEffect("Maximum attempts reached. Exiting program.")
    sys.exit()


#Password confirmation function
def pswConf():
    conf = typingEffectInput("To log-in, input your password. ")
    if conf == password:
        typingEffect(f"Welcome, {username}!")
    else:
        text = f"{conf} is not your password!"
        typingEffect(text, speed)
        exit();
pswConf()

def main():
    selection = typingEffectInput(f"What do you want today, {username}?\n Options: Calculator. ")
    if selection == "Calculator":
        selec2 = typingEffectInput("Which type of calculator?\n Sum\n Subtraction\n Division\n")
        if selec2 == "Sum":
            try:
                x = float(typingEffectInput("What's x? "))
            except ValueError:
                typingEffect("Not a valid number!")
                time.sleep(5)
                exit()
            try:
                y = float(typingEffectInput("What's y? "))
            except ValueError:
                typingEffect("Not a valid number!")
                time.sleep(5)
                exit()
            z = round(x + y)

            typingEffect(f"{z:,}")
            time.sleep(5)

        if selec2 == "Subtraction":
            try:
                x = float(typingEffectInput("What's x? "))
            except ValueError:
                typingEffect("Must be a number!")
                time.sleep(5)
                exit()
            try:
                y = float(typingEffectInput("What's y? "))
            except ValueError:
                typingEffect("Must be a number!")
                time.sleep(5)
                exit()
            z = round(x - y)

            typingEffect(f"{z:,}")
            time.sleep(5)

        if selec2 == "Division":
            try:
                x = float(typingEffectInput("What's x? "))
            except ValueError:
                typingEffect("This is not a number!")
                time.sleep(5)
                exit()
            try:
                y = float(typingEffectInput("What's y? "))
            except ValueError:
                typingEffect("This is not a number!")
                time.sleep(5)
                exit()
            z = round(x / y)

            typingEffect(f"{z:,}")
            time.sleep(5)

    else:
        typingEffect("That's not a valid option!")
        time.sleep(5)
        exit()


main()