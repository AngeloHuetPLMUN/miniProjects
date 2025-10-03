import secrets
import string


def pass_preferences():
    try:
        pw_length = int(input("Password Length: "))
        if pw_length < 6:
            print("Password to short Must be at least 6 characters or above.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    user_want = input(
        "What types of characters do you want to include? (U = Uppercase, L = Lowercase, N = Numbers, S = Symbols). Type the letters together: ").upper()

    characters = ""

    if 'U' in user_want:
        characters += string.ascii_uppercase
        print("Include Uppercase")
    if 'L' in user_want:
        characters += string.ascii_lowercase
        print("Include Lowercase")
    if 'N' in user_want:
        characters += string.digits
        print("Include Numbers")
    if 'S' in user_want:
        characters += string.punctuation
        print("Include Symbols")
    if not characters:
        print("No character types selected! Try again bitch.")
        return

    password = "".join(secrets.choice(characters) for _ in range(pw_length))
    print(f"Your Generated password: {password}")


while True:
    pass_preferences()
    again = input("\nDo you want to generate again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! 🌵")
        break
