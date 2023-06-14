import time

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