from typing_effects import *

def power():
        selec3 = typingEffectInput("Square, Cube...? ").capitalize()
        if selec3 == "Square":
            x = float(typingEffectInput("What's x? "))
            z = round(x ** 2)
        elif selec3 == "Cube":
            x = float(typingEffectInput("What's x? "))
            z = round(x ** 3)

        typingEffect(f"The power of {x} is: {z:,}")
        time.sleep(5)

def sum(x, y):
    z = round(x + y)
    typingEffect(f"{z:,}")
    time.sleep(5)

def subtract(x, y):
    z = round(x - y)
    typingEffect(f"{z:,}")
    time.sleep(5)

def divide(x, y):
    z = round(x / y)
    typingEffect(f"{z:,}")
    time.sleep(5)

def multiply(x, y):
    z = round(x * y)
    typingEffect(f"{z:,}")
    time.sleep(5)
