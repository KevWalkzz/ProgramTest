import time
from typing_effects import typingEffect, typingEffectInput


def square(n):
    return n * n


def calculator(username):
    selection = typingEffectInput(
        f"What do you want today, {username}?\nOptions: Calculator. ")
    if selection.capitalize() == "Calculator":
        selec2 = typingEffectInput("Which type of calculator?\nSum\nSubtraction\nDivision\nMultiplication\nPower\n").capitalize()

        if selec2 == "Power":
            x = float(typingEffectInput("What's x? "))
            z = round(square(x))

            typingEffect(f"{z:,}")
        else:
            try:
                x = float(typingEffectInput("What's x? "))
                y = float(typingEffectInput("What's y? "))

                if selec2 == "Sum":
                    z = round(x + y)
                elif selec2 == "Subtraction":
                    z = round(x - y)
                elif selec2 == "Division":
                    z = round(x / y)
                elif selec2 == "Multiplication":
                    z = round(x * y)
                else:
                    typingEffect("That's not a valid option!")
                    time.sleep(5)
                    exit()

                typingEffect(f"{z:,}")
                time.sleep(5)

            except ValueError:
                typingEffect("Invalid input. Please enter numbers only!")
                time.sleep(5)
                exit()

    else:
        typingEffect("That's not a valid option!")
        time.sleep(5)
        exit()

        pass
