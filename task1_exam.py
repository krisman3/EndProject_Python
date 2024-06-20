### Task 1 ###
# Rock/Paper/Scissors
# Since this is played in the console - you will default to Player 1
import random

choice_dict = {1: "Rock", 2: "Paper", 3: "Scissors"}


def choices():
    print("1 = Rock")
    print("2 = Paper")
    print("3 = Scissors")
    choice = int(input("Your choice: "))

    if choice != 1 and choice != 2 and choice != 3:
        return "Please do a valid selection!"
    else:
        return choice


def random_player2():
    return random.randint(1, 3)


def check_choices(player1, player2):
    if player1 == 1:
        if player2 == 1:
            print(f"You selected: {choice_dict[player1]}")
            print("Draw!")
            return
        elif player2 == 2:
            print(f"You selected: {choice_dict[player1]}")
            print("Paper beats rock.")
            print("You lose.")
            return
        elif player2 == 3:
            print(f"You selected: {choice_dict[player1]}")
            print("Rock beats Scissors.")
            print("You win!")
            return

    if player1 == 2:
        if player2 == 1:
            print(f"You selected: {choice_dict[player1]}")
            print("Paper beats rock.")
            print("You win!")
            return
        elif player2 == 2:
            print(f"You selected: {choice_dict[player1]}")
            print("Draw!")
            return
        elif player2 == 3:
            print(f"You selected: {choice_dict[player1]}")
            print("Scissors beat paper.")
            print("You lose.")
            return

    if player1 == 3:
        if player2 == 1:
            print(f"You selected: {choice_dict[player1]}")
            print("Rock beats scissors.")
            print("You lose.")
            return
        elif player2 == 2:
            print(f"You selected: {choice_dict[player1]}")
            print("Scissors beats paper.")
            print("You win!")
            return
        elif player2 == 3:
            print(f"You selected: {choice_dict[player1]}")
            print("Draw!")
            return


def continue_prompt():
    choice = input("Do you want to play again? (Y/N)").lower()
    if choice == "y":
        return True
    elif choice == "n":
        return False
    else:
        print("Incorrect choice. Please choose Y or N")
        return continue_prompt()


# Main logic of the game

# Your choice (player 1)
while True:
    try:
        player1_choice = choices()
        player2_choice = random_player2()
    except ValueError:
        print("Incorrect choice. Please select a valid value!")
        continue

    check_choices(player1_choice, player2_choice)

    game_on = continue_prompt()

    if not game_on:
        break
