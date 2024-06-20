### Task 2 ###
import random

# Guess the number

lower_range = 1
upper_range = 10


def random_number():
    return random.randint(1, 10)


def player_name():
    while True:
        name = str(input("Enter your name: "))
        if name != '':
            return name
        print("Name can't be empty.")
        print()


def player_guess():
    global lower_range, upper_range
    while True:
        try:
            guess = input("Your guess: ")
            if guess == '':
                print("This field cannot be empty!")
                continue
            elif not guess.isdigit():
                print(f"The guess must be an integer from {lower_range} to {upper_range}!")
                continue
            if guess.isdigit():
                if lower_range <= int(guess) <= upper_range:
                    return guess
        except ValueError:
            # Hard-coded the values for easier implementation
            print(f"Please enter an integer from {lower_range} to {upper_range}!")


