import sys
import random
from enum import Enum

game_count = 0

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # input player choice
    playerchoice = input("\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

    # validate input
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    # change player choice in integer
    player = int(playerchoice)

    # genrate random choice of computer
    computerchoice = random.choice("123")

    # change compurt(Python) choice in integer
    computer = int(computerchoice)

    # print computer(python) choice and player choice
    print("\nYou chose : " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose : " + str(RPS(computer)).replace('RPS.', '') + ".\n")

    # winner declaration 
    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🎉 You Win!"
        elif player == 2 and computer == 1:
            return "🎉 You Win!"
        elif player == 3 and computer == 2:
            return "🎉 You Win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            return "🐍 Python Wins!"
    game_result = decide_winner(player, computer)
    print(game_result)

    global game_count 
    game_count  += 1
    print("\n Game Count:  " + str(game_count))

    print("\nPlay again?")

    while True:
        playagain = input("\nY for Yes or \nQ to Quit \n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n 🎉🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")
play_rps()
