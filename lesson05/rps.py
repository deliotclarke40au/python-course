import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😲 Tie game!")
else:
    print("🐍 Python wins!")

def printUserInput():
    printValue = input("\nYou chose to print your own input, what would you like to print:\n")
    print(printValue)

def acceptArgs(*args):
    print(args)

print('')
print("Let's play a new game, Function caller 101!!")

functionToCall = input("\nEnter PRINT to print your own input or end ARGS to print multiple arguments\n")

if functionToCall == 'PRINT':
    printUserInput()
elif functionToCall == 'ARGS':
    arguments = input('\nWhat arguments would you like to submit?\n')
    acceptArgs(arguments)
else:
    print('\nWhat are you even talking about?')


quit()
