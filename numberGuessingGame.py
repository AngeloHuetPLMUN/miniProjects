# numberGuessingGame Done✅
# new mini project 09/25/2025

import random


def main():
    secret_number = random.randint(1, 100)
    attempts = 0
    MAX_ATTEMPTS = 10
    print("You only have 10 attempts!", end="")
    while True:
        try:
            guess_number = int(input("\nGuess random number from 1-100: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess_number > 100 or guess_number < 1:
            print("You cannot go higher than 100 and lower than 1!")
            continue

        attempts += 1

        if guess_number < secret_number:
            print("Too Low, Try again.")
        elif guess_number > secret_number:
            print("Too High, Try again.")
        else:
            print(f"Nice You Won in {attempts} attempts!")
            break

        if attempts == 5:
            print(f"You have {attempts} attempts left!")
        elif attempts == MAX_ATTEMPTS:
            print(
                f"You used all {attempts} attempts you lose! 😭 tanga ka kase!")
            break


while True:
    main()
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! 🌵")
        break
