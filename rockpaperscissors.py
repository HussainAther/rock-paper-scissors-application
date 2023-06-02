import random

def player_choose():
    """
    Rock-paper-scissors game in which a player chooses
    an option (rock, paper, scissors). 

    The player chooses using this function.
    """
    options = ["Rock", 
                     "Paper", 
                     "Scissors"]
    while True:
        choice = input("Choose your option (Rock/Paper/Scissors): ")
        if choice in options:
            return choice
        print("Not a valid option. Please try again.")

def computer_choose():
    """
    The computer chooses an option. 
    """
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)

def game_logic(player_choice, computer_choice):
    """
    Define the logic of the game.
    Who wins based on the options?
    """
    if player_choice == computer_choice:
        return "Draw"
    elif player_choice == "Rock" and computer_choice == "Paper":
        return "You lose" 
    elif player_choice == "Paper" and computer_choice == "Rock":
        return "You win"
    elif player_choice == "Scissors" and computer_choice == "Paper":
        return "You win"
    elif player_choice == "Paper" and computer_choice == "Scissors":
        return "You lose"
    elif player_choice == "Rock" and computer_choice == "Scissors":
        return "You win"
    elif player_choice == "Scissors" and computer_choice == "Rock":
        return "You lose"
    
def play_game():
    pc = player_choose()
    cc = computer_choose()
    output = game_logic(pc, cc)

play_game()