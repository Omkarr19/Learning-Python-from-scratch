# Rock Paper Scissors
import random

option = ("rock", "paper", "scissors")  # tuple is fine since options won't change
running = True

while running:

    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a Tie!!!!")
    elif player == "rock" and computer == "scissors":
        print("You Win!!!!!!!!")
    elif player == "paper" and computer == "rock":
        print("You Winnn!!!!!!!")
    elif player == "scissors" and computer == "paper":
        print("You Winn!!!!")
    else:
        print("You looseee cryyyy innn cornerrr lmaooo xD")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        running = False

print("Thanks for playing ❤️")
