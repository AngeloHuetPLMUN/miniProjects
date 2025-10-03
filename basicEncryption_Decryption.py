def get_user_text():
    user_text = input("Enter Text: ")
    user_ask = input("(E)ncrypt or (D)ecrypt: ")
    return user_text, user_ask


def validate_input(user_text, user_ask):
    if not user_text:
        print("Error: Text cannot be empty!")
        return False

    if user_ask.upper() not in ("E", "D"):
        print("Error: Choice must be 'E' for Encrypt or 'D' for Decrypt!")
        return False

    return True


def encryption_decryption():
    while True:
        method = input(
            "\"C\" for Caesar, \"R\" for Reverse, \"S\" for Substitution: ").upper()
        if method == 'C':
            print("Caesar Cipher selected.")
            return method
        elif method == 'R':
            print("Reversed Text selected.")
            return method
        elif method == 'S':
            print("Substitution selected.")
            return method
        else:
            print("Invalid choice, Please select C, R, or S.")


def transform_text(text, method, key=3, action="E"):
    result = ""

    if method == 'C':
        for char in text:
            if char.isalpha():
                if char.isupper():
                    start = ord('A')
                else:
                    start = ord('a')

                shift = key if action == "E" else -key
                result += chr((ord(char) - start + shift) % 26 + start)
            else:
                result += char

    elif method == 'R':
        result = text[::-1]

    elif method == 'S':
        sub_map = {
            'a': '@', 'b': '8', 'c': '(', 'd': 'D', 'e': '3', 'f': 'F', 'g': '6',
            'h': '#', 'i': '!', 'j': 'J', 'k': 'K', 'l': '1', 'm': 'M', 'n': 'N',
            'o': '0', 'p': 'P', 'q': 'Q', 'r': 'R', 's': '$', 't': '7', 'u': 'U',
            'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': '2'
        }
        if action == "E":
            for char in text:
                result += sub_map.get(char.lower(), char)
        else:
            inv_map = {v: k for k, v in sub_map.items()}
            for char in text:
                result += inv_map.get(char, char)

    return result


while True:
    user_text, user_ask = get_user_text()
    if not validate_input(user_text, user_ask):
        continue

    method = encryption_decryption()

    key = 3
    if method == 'C':
        try:
            key_input = int(input("Enter key for Caesar Cipher (default 3): "))
            key = key_input
        except ValueError:
            print("Invalid key, using default 3.")

    final_result = transform_text(
        user_text, method, key, action=user_ask.upper())
    print(f"\nResult: {final_result}")

    again = input("\nDo you want to process another text? (y/n): ").lower()
    if again != 'y':
        print("Thanks for using the Encryption/Decryption Tool! 🌟")
        break
