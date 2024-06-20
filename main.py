### Task 2 ###
import random


# Guess the number

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

