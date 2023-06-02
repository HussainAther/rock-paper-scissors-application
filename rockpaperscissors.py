#Game done by Hussain and Saraa

import random

def player_choose():
    """
    Rock-paper-scissors game in which a player chooses
    an option (rock, paper, scissors). 

    The player chooses using this function.
    """
    options = ["rock", 
                     "paper", 
                     "scissors"]
    while True:
        choice = input("Choose your option (Rock/Paper/Scissors): ")
        if choice.lower() in options:
            return choice
        print("Not a valid option. Please try again.")

def computer_choose():
    """
    The computer chooses an option. 
    """
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def game_logic(player_choice, computer_choice):
    """
    Define the logic of the game.
    Who wins based on the options?
    """
    if player_choice == computer_choice:
        return "Draw"
    elif player_choice == "rock" and computer_choice == "paper":
        return "You lose" 
    elif player_choice == "paper" and computer_choice == "rock":
        return "You win"
    elif player_choice == "scissors" and computer_choice == "paper":
        return "You win"
    elif player_choice == "paper" and computer_choice == "scissors":
        return "You lose"
    elif player_choice == "rock" and computer_choice == "scissors":
        return "You win"
    elif player_choice == "scissors" and computer_choice == "rock":
        return "You lose"
    
def play_game():
    pc = player_choose()
    cc = computer_choose()
    print("Computer choose " + cc)
    output = game_logic(pc, cc)
    print(output)

    while True:
        play_again = input("Would you like to play again? [Yes/I quit] ")
        if play_again == "I quit":
            print("Thank you for playing! ")
            quit()
        elif play_again.lower() == "yes":
            play_game()
        else:
            print("Invalid choice, try again")

            
            

play_game()