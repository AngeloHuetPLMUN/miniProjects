# Ask the user for input and count how many digits are in the text.
text = input("Enter text: ")

count = 0
for char in text:
    if char.isdigit():
        count += 1

print(f"There are {count} digits in \"{text}\".")
