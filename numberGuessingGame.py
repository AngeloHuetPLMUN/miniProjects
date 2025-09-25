# numberGuessingGame Done✅
# new mini project 09/25/2025

import random


def main():
    secret_number = random.randint(1, 100)
    attempts = 0
    MAX_ATTEMPTS = 10
    MIN = 1
    MAX = 100

    print("\nYou only have 10 attempts!", end="")
    while True:
        try:
            guess_number = int(input("\nGuess random number from 1-100: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess_number > MAX or guess_number < MIN:
            print("Number must be between 1 and 100! engot?")
            continue

        attempts += 1

        if guess_number < secret_number:
            print("Too Low, Try again.")
        elif guess_number > secret_number:
            print("Too High, Try again.")
        else:
            print(f"Nice! You Won in {attempts} attempts!")
            break

        if attempts == 5:
            print(f"You have {MAX_ATTEMPTS - attempts} attempts left!")
        elif attempts == MAX_ATTEMPTS:
            print(
                f"You used all {attempts} attempts you lose! 😭 tanga ka kase!\n")
            print(f"The secret number was {secret_number}.")
            break


while True:
    main()
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! 🌵")
        break
