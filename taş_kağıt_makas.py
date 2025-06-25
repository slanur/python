import random

def get_player_choice():
    player_choice = input("enter a choice(rock,paper,scissors):")
    return player_choice


def get_computer_choice():
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    return computer_choice


def check_win(player, computer):
    if (player==computer):
        return "It's a tie!"
    
    elif (player=="rock" and computer=="scissors"):
        return "Rock smashes scissors! You won!"
    
    elif (player=="rock" and computer=="paper"):
        return "Paper cover rock! You lost!"
    
    elif (player=="paper"):
        if (computer=="rock"):
            return "Paper covers rock! You win!"
        else:
            return "Scissors cut paper! You lose."
         
    elif (player=="scissors"):
        if (computer=="paper"):
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."      


player_choise= get_player_choice()
computer_choice=get_computer_choice()
result=check_win(player_choise,computer_choice)
print(f"computer choice is {computer_choice}")
print(result)