from user import User
from calculator import calculator
from passconfirm import password_confirmation
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

if __name__ == "__main__":
    main()
