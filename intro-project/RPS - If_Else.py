# libraries
# import random


# lists
# food = ["biriyani", "polaw", "kichuri", "kabab", "halim"]
# print(food)

import random                                                           #libraries
def get_choices():                                                      #user defined function
    player_choice = input("Enter a Choice(rock/paper/scissors): ")      #taking input
    options = ["rock", "paper", "scissors"]                             #lists
    computer_choices = random.choice(options)                           #library methods
    choices = {"Player": player_choice, "Computer": computer_choices}   #dictionaries

    return choices                  

# choices = get_choices()            #calling function                                    
# print(choices)                     #printing through calling function in variable    

# Function Arguments
def check_win(player, computer):
    return [player, computer]
    
    # if and else in Python
    if player == computer:
        return "It's a Tie!"
    else:
        return "It isn't Tie."
