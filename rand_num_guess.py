#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: Oct 07
# This program checks if a user's integer guess is correct to the computer's generated number

# imports random
import random


def main():
    # assigns a random number from 0-9 to the secret_number variable
    secret_number = random.randint(0, 9)

    # asks the user for input (their guess)
    print("The secret number is between 0-9")
    user_guess = float(input("Enter your guess: "))

    # check if the user's guess matches secret_number and output if statement is correct
    if secret_number == user_guess:
        print("Your guess is right!")

    # else, if the user guessed incorrectly
    else:
        print(f"You guessed incorrectly, The correct answer was {secret_number}")


if __name__ == "__main__":
    main()
