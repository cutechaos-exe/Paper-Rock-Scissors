# paper, rock, scissors game
import random

guess = random.randint(1, 3) #paper = 1, rock = 2, scissors = 3
if guess == 1:
    answer = "paper"
elif guess == 2:
    answer = "rock"
else:
    answer = "scissors"

player_guess = input("Choose paper, rock, or scissors ").lower()
if player_guess == "paper" or player_guess == "rock" or player_guess == "scissors":
    if player_guess == "paper":
        player = 1
    elif player_guess == "rock":
        player = 2
    else:
        player = 3
else:
    print("Wrong input")
    exit()

print("I chose "+ answer)
if (player == 1 and guess == 2) or (player == 2 and guess == 3) or (player == 3 and guess == 1):
    print("You win!")
elif player == guess:
    print("It is a tie!")
else:
    print("You lose!")