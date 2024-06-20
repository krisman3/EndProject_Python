### Task 2 ###
import random

# Guess the number

lower_range = 1
upper_range = 10


def random_number():
    return random.randint(1, 10)


def player_name():
    incorrect = True
    while incorrect:
        name = str(input("Enter your name: "))
        if name != '':
            incorrect = False
            return name
        print("Name can't be empty.")
        print()


def player_guess(actual_num):
    global lower_range, upper_range
    while True:
        try:
            guess = input("Your guess: ")
            if guess.isdigit():
                if lower_range <= int(guess) <= upper_range:
                    return guess
        except ValueError:
            print(
                f"Please enter an integer from {lower_range} to {upper_range}!")  # Hard-coded the values for easier implementation


