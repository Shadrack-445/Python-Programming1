import random

def game():
    player = input("Choose between rock, paper or scissors:")
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    choices = {"Player_Choice":player , "Computer_Choice":computer}
    return choices

def results(player,computer):
    print(f"Player chose {player} , Computer chose {computer}")
    if player == computer :
        return "It's a tie"
    
    elif player == "rock":
        if computer == "paper":
            return "You lose"
        else: 
            return "You win"
        
    elif player == "paper":
        if computer == "scissors":
            return "You lose"
        else:
            return "You win"
        
    elif player == "scissors":
        if computer == "rock":
            return "You lose"
        else:
            return "You win"
        
    
game_choices = game()
winner = results(game_choices["Player_Choice"],game_choices["Computer_Choice"])
print(winner)
    

    

    




    