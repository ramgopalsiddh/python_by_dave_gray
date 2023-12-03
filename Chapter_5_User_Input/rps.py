import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(" ")
# input player choice
playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

# change player choice in integer
player = int(playerchoice)

# validate input
if player < 1 | player > 3:
    sys.exit("You must enter 1, 2, or 3.")

# genrate random choice of computer
computerchoice = random.choice("123")

# change compurt(Python) choice in integer
computer = int(computerchoice)

print("")
# print computer(python) choice and player choice
print("You chose : " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose : " + str(RPS(computer)).replace('RPS.', '') + ".")

print(" ")


# winner declaration 
if player == 1 and computer == 3:
    print("🎉 You Win!")
elif player == 2 and computer == 1:
    print("🎉 You Win!")
elif player == 3 and computer == 2:
    print("🎉 You Win!")
elif player == computer:
    print("😲 Tie game!")
else:
    print("🐍 Python Wins!")
