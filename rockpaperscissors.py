def get_player_choice():
    """
    Rock-paper-scissors game in which a player chooses
    an option (rock, paper, scissors). 
    """
    valid_choices = ["Rock", "Paper", "Scissors"]
    while True:
        choice = input("Choose your option (Rock/Paper/Scissors): ")
        if choice in valid_choices:
            return choice
        print("Not a valid option. Please try again.")

