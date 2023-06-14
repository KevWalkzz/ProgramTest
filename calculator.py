import time
from calculadora.math_operations import *
from typing_effects import typingEffect, typingEffectInput


def calculator():
    selec2 = typingEffectInput("Which type of calculator?\nSum\nSubtraction\nDivision\nMultiplication\nPower\n").capitalize()

    if selec2 == "Power":
        power()

    elif selec2 in ["Sum", "Subtraction", "Division", "Multiplication"]:

        x = float(typingEffectInput("What's x? "))
        y = float(typingEffectInput("What's y? "))

        if selec2 == "Sum":
            sum(x, y)
        elif selec2 == "Subtraction":
            subtract(x, y)
        elif selec2 == "Division":
            divide(x, y)
        elif selec2 == "Multiplication":
            multiply(x, y)

    else:
        typingEffect("Looks like the calculator doesn't have that function yet!")
        time.sleep(5)
        exit()
