### Task 2 ###
import random

# Guess the number


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
    lower_range = 1
    upper_range = 10
    while True:
        try:
            guess = int(input(f"Your guess (from {lower_range} to {upper_range}): "))
            if guess == '':
                print("This field cannot be empty!")
                continue
            return guess
        except ValueError:
            print(f"Please enter an integer from {lower_range} to {upper_range}!")
            print('\n')
            continue


def guess_check(player_num: int, actual_num: int):
    if player_num == actual_num:
        return True
    else:
        return False


def lower_or_higher(player_num: int, actual_num: int):
    if player_num < actual_num:
        return "Go higher!"
    elif player_num > actual_num:
        return "Go lower!"


### Main logic of the game: ###

# Initializing the attempts counter:
count = 1

# Generating a random number to guess:
rand_num = random_number()
while True:

    # Player choice is entered here:
    pl_choice = player_guess()

    # Numbers are checked:
    check_game = guess_check(pl_choice, rand_num)
    if check_game:
        print(f"Congratulations! You won. It took you {count} tries.")
        break
    # If they're not equal, player gets feedback
    else:
        count += 1
        print(lower_or_higher(pl_choice, rand_num))
