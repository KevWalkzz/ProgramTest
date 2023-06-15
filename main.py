from user import User
from features.calculadora import *
from typing_effects import typingEffect, typingEffectInput


def main():
    user = User()
    
    while user.validate_email(typingEffectInput("Please, insert your email: ").strip()) == False:
        typingEffect("Invalid email, try again")
        
    while user.validate_user(typingEffectInput("What's your name? ").strip()) == False:
        typingEffect("Invalid username, try again")

    while user.validate_password(password = typingEffectInput("Please, insert your password: ").strip()) == False:
        typingEffect("Invalid password, try again")
    
    typingEffect("user created successfully")

    typingEffect("To log into your account insert your email, username and password")

    while user.login(email=typingEffectInput("Email: "), user=typingEffectInput("Username: "), password=typingEffectInput("Password: ")) == False:
        typingEffect("Log in failed, try again")

    typingEffect("Log in successfully")

    while typingEffectInput(f"What do you want today, {user.get_user()}? Options: Calculator. ").capitalize() not in ["Calculator"]:
        typingEffect("That's not a valid option!, try again")

    while True:
        operation = typingEffectInput("Which type of calculator?\nSum\nSubtraction\nDivision\nMultiplication\nPower\n").capitalize()

        if operation == "Power":
            type_figure = typingEffectInput("Square, Cube...? ").capitalize()
            x = float(typingEffectInput("What's x? "))

            if type_figure == "Square":
                typingEffect(f"The square of {x}² == {power(x,2)}")
            elif type_figure == "Cube":
                typingEffect(f"The square of {x}³ == {power(x,3)}")

        elif operation in ["Sum", "Subtraction", "Division", "Multiplication"]:

            x = float(typingEffectInput("What's x? "))
            y = float(typingEffectInput("What's y? "))

            if operation == "Sum":
                typingEffect(f"The sum of {x} + {y} == {sum(x, y)}")
            elif operation == "Subtraction":
                typingEffect(f"The subtraction of {x} - {y} == {subtract(x, y)}")
            elif operation == "Division":
                typingEffect(f"The division of {x} / {y} == {divide(x, y):.2f}")
            elif operation == "Multiplication":
                typingEffect(f"The multiplication of {x} * {y} == {multiply(x, y)}")

        else:
            typingEffect("Looks like the calculator doesn't have that function yet! choice another")



if __name__ == "__main__":
    main()
