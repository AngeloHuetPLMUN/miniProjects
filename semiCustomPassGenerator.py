# improvedRandomNumberGenerator Done✅
# new mini project 10/03/2025

import secrets
import string


def get_user_base():
    preferred_word = input("Enter your base password: ")
    if len(preferred_word) < 4:
        print("Password too short! Must be at least 4 characters.")
        return None
    else:
        return preferred_word


def choose_addons():
    user_want = input(
        "Do you want (U = Uppercase, N = Numbers, S = Symbols)? Type the letters together: "
    ).upper()

    characters = ""

    if 'U' in user_want:
        characters += string.ascii_uppercase
        print("Uppercase included!")
    if 'N' in user_want:
        characters += string.digits
        print("Numbers included!")
    if 'S' in user_want:
        characters += string.punctuation
        print("Symbols included!")

    if not characters:
        print("No character types selected! Try again.")
        return

    return characters, user_want


def generate_final_password(preferred_word, user_want, characters):
    try:
        extra_chars = int(input("\nHow many random characters to add? "))
        if extra_chars <= 0:
            print("Invalid input! Must use positive number.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if 'U' in user_want:
        preferred_word = preferred_word.upper()
    random_chars = ''.join(secrets.choice(characters)
                           for _ in range(extra_chars))
    final_password = preferred_word + random_chars

    print("\nYour final generated password is:", final_password)


while True:
    preferred_word = get_user_base()
    if preferred_word:
        characters, user_want = choose_addons()
        if characters:
            generate_final_password(preferred_word, user_want, characters)
    again = input("\nDo you want to generate again? (y/n): ").lower()
    if again != "y":
        print("Thanks for generating! 🌵")
        break
