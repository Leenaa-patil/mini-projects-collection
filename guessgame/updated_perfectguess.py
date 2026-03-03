# generate a random number abd ask user to guess it. "higher number please"- guesss<number. "lowernumber please"- guess>number
"""
Perfect Guess Game.
This module implements a simple interactive number-guessing game. A random
target integer in the range 1–100 is chosen and the user is repeatedly prompted
to guess the number. After each guess the program indicates whether the
target is higher or lower than the guess. Non-integer input is handled and
prompts the user to enter a valid number.
Behavior:
- Chooses a random integer in [1, 100].
- Reads guesses from standard input.
- Increments an attempt counter for each valid integer guess.
- Responds with a hint ("Higher number please" or "Lower number please") until
    the correct number is guessed.
- On a correct guess prints a win message and a final analysis summary that
    includes game status, the target number, and total attempts.
Usage:
- Run the script and follow the on-screen prompts. No function arguments or
    return values; the script exits after printing the final analysis.
"""
import random

n = random.randint(1, 100)

print("*" * 40)
print("PERFECT GUESS GAME")
print("*" * 40)

a=-1
attempts = 0
response_if_win = "*-yay! you won-*"

while True:
    try:
        a = int(input("What's your guess? (1-100): "))
        attempts += 1

        if a < n:
            print("Higher number please")
        elif a > n:
            print("Lower number please")
        else:
            print(f"\n{response_if_win}")
            break

    except ValueError:
        print("Please enter a valid number.")

print("-" * 30)
print("ANALYSIS:\n")
print(f"Game status: {'won'}")
print(f"Target number: {n}")
print(f"Attempts: {attempts}")
