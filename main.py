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
    while True:
        try:
            guess = input("Your guess: ")
        except ValueError:
            print("Please enter an integer from 1 to 10!")  # Hard-coded the values for easier implementation
        if guess.isdigit()