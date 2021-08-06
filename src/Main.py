"""
Project: Old Gold Game
Author:  Travis Byrman
School:  Waimea College
Date:    September 2018
Module:  Main.py
Purpose: The main program file for the game, this is how Old Gold operates
"""
# --------------------------------------------------------------------------------------------------------------------------------

from random import randint
from Input import *
from Output import *
import random
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

GOLD_COIN = " 0 "  # What silver coins will look like
SILVER_COIN = " O "  # What gold coins will look like

GRID_MIN = 10  # Minimum grid size the user can have
GRID_MAX = 30  # Maximum grid size the user can have

COIN_MIN = 2  # Minimum amount of coins user can have
COIN_MAX = 30  # Maximum amount of coins user can have

# --------------------------------------------------------------------------------------------------------------------------------


def PLAY(PLAYERS, GRID):
    COIN_SELECT = inputNumber("{}, what coin would you like to select to be moved? ".format(
        PLAYERS), 1, GRID_SIZE)  # Asks for users coin they want to move.
    # Computer starts at 0 on the number line, humans start at 1, changes the number
    PC_COIN_SELECT = (COIN_SELECT) - 1
    COIN_DETECT = (COIN_SELECT) - 2
    COIN_AUTO_MOVE = (COIN_SELECT) - 3

    if GRID[PC_COIN_SELECT] == "   ":  # If the place selected is not a coin
        print("Please select a coin")
        return PLAY(PLAYERS, GRID)  # Players turn again

    # If coin is in left spot of coin selected, coin will not move.
    if PC_COIN_SELECT >= 1 and GRID[COIN_DETECT] != "   ":
        print("That coin cannot be moved")
        return PLAY(PLAYERS, GRID)  # Redo players turn

    # If the coin selected is > 1 and there is a coin in the 2nd spot to the left of coin, auto move coin
    if COIN_SELECT > 1 and GRID[COIN_AUTO_MOVE] != "   " or COIN_SELECT == 2 and GRID[0] == "   ":
        # If the coin selected is in the 2nd spot and there is not a coin in the first spot, auto move coin.
        GRID[COIN_DETECT] = GRID.pop(PC_COIN_SELECT)
        # insert blank into the old coin spot.             #Else, ask user where they want to move to
        GRID.insert(PC_COIN_SELECT, "   ")
        BOX(GRID)  # Displaying items in grid in boxes
        NUMBER_LINE(GRID)  # Displaying number line under boxes
        return

    # If the user enters 1 to remove a coin and its gold
    if COIN_SELECT == 1 and GRID[0] == GOLD_COIN:
        GRID.pop(0)  # Remove gold coin
        GRID.insert(0, "   ")  # Insert a blank
        BOX(GRID)  # Display items in box
        NUMBER_LINE(GRID)
        # Print winner
        print("────────────────────────────────────────────────────────")
        print("Congratulations! {} is the winner!".format(PLAYERS))
        print("────────────────────────────────────────────────────────")
        return

    # But if user enters 1 and its a silver coin
    elif COIN_SELECT == 1 and GRID[0] == SILVER_COIN:
        GRID.pop(0)  # Remove the silver coin
        GRID.insert(0, "   ")  # Insert a blank
        # Print the player has removed a coin
        print("────────────────────────────────────────────────────────")
        print("{} removed a silver coin!".format(PLAYERS))
        print("────────────────────────────────────────────────────────")
        BOX(GRID)  # Displaying items in grid in boxes
        NUMBER_LINE(GRID)  # Displaying number line under boxes
        return

    if GRID[PC_COIN_SELECT] == GOLD_COIN:
        GRID.pop(PC_COIN_SELECT)  # Remove the silver coin
        GRID.insert(PC_COIN_SELECT, "→0←")  # Insert a blank
        BOX(GRID)
        NUMBER_LINE(GRID)
        GRID.pop(PC_COIN_SELECT)  # Remove the silver coin
        GRID.insert(PC_COIN_SELECT, " 0 ")  # Insert a blank

    if GRID[PC_COIN_SELECT] == SILVER_COIN:
        GRID.pop(PC_COIN_SELECT)  # Remove the silver coin
        GRID.insert(PC_COIN_SELECT, "→O←")  # Insert coin with arrows
        BOX(GRID)  # Print box with arrows and coin
        NUMBER_LINE(GRID)  # Prints number line
        GRID.pop(PC_COIN_SELECT)  # Remove the coin with arrows
        # Reverts back to previous coin, doesnt show user coin without arrows. This is for the PC to identify the coin.
        GRID.insert(PC_COIN_SELECT, " O ")

# --------------------------------------------------------------------------------------------------------------------------------

    COIN_MOVE = inputNumber("How many places to the left would you like the coin to be moved? ",
                            1, COIN_SELECT - 1)  # User inputs the amount of places the coin moves
    PC_COIN_MOVE = (COIN_MOVE) - 1
    # Since PC counts 0 as the first digit unlike us where we count 1 as, we are converting.
    COIN_NEW_PLACE = (PC_COIN_SELECT) - (PC_COIN_MOVE) - 1

    for x in range(COIN_NEW_PLACE, PC_COIN_SELECT):
        if GRID[x] != "   ":  # If an index is not blank
            BOX(GRID)  # Displaying items in grid in boxes
            NUMBER_LINE(GRID)  # Displaying number line under boxes
            print("Invalid turn, please select coin and try again")
            PLAY(PLAYERS, GRID)  # Redo players turn
            break

        # When x is appplying first if statement on first index, begin going through all indexes.
        elif x == PC_COIN_SELECT - 1:
            # If index is blank, remove coin and insert it into users selected spot
            GRID[COIN_NEW_PLACE] = GRID.pop(PC_COIN_SELECT)
            # insert blank into the old coin spot.
            GRID.insert(PC_COIN_SELECT, "   ")
            BOX(GRID)  # Displaying items in grid in boxes
            NUMBER_LINE(GRID)  # Displaying number line under boxes

# --------------------------------------------------------------------------------------------------------------------------------


while True:

    GRID_SIZE = 18  # Default Grid Size
    NUM_COINS = 6  # Default Number of Coins

    print("────────────────────────────────────────────────────────\n")
    print("                 Welcome to Old Gold!")
    print("\n────────────────────────────────────────────────────────")

    # Instructions input
    HELP = inputTextYN("Would you like the instructions? (Yes/No) ")
    # If input is 'Yes' instructions will be displayed, If input is 'No' instructions will not be displayed.
    if HELP.lower() == "yes":
        INSTRUCTIONS()
    else:
        print("────────────────────────────────────────────────────────")

    print("Enter your names to continue!")
    print("────────────────────────────────────────────────────────")
    P1 = inputText("Player 1, what is your name? ")  # Enter player names
    P2 = inputText("Player 2, what is your name? ")
    print("────────────────────────────────────────────────────────")
    PLAYERS = [P1, P2]  # Player names added into a list
    random.shuffle(PLAYERS, random.random)  # random shuffle players

    DEFAULT = inputTextYN(
        "Would you like to use the default settings?\nGrid Size is 18 boxes, Number of Coins is 6 (Yes/No) ")
    # If input is 'No' game options will be asked If input is 'Yes' default options are used.
    if DEFAULT.lower() == "no":
        print("────────────────────────────────────────────────────────")
        # Asks for users grid size
        GRID_SIZE = inputNumber(
            "How big would you like the grid? ", GRID_MIN, GRID_MAX)
        # Asks for how many coins the user wants to use
        NUM_COINS = inputNumber(
            "How many coins would you like to use? ", COIN_MIN, GRID_SIZE)
    else:
        print("────────────────────────────────────────────────────────")

    GRID = ["   "] * GRID_SIZE  # Filling grid with blank items
    GRID.append(GOLD_COIN)  # Adding the gold into the grid
    COINS = [SILVER_COIN] * NUM_COINS  # Adding silver coins into list
    del COINS[:1]  # Deletes one silver coin to accommodate for gold coin
    del GRID[:NUM_COINS]  # Removing blank items to accommodate all coins
    GRID.extend(COINS)  # Adding coins to grid
    # Randomising grid, coins and spaces are anywhere.
    random.shuffle(GRID, random.random)
    BOX(GRID)  # Displaying items in grid in boxes
    NUMBER_LINE(GRID)  # Displaying number line under boxes

# --------------------------------------------------------------------------------------------------------------------------------

    for item in GRID:
        if GOLD_COIN in GRID:  # If gold coin still in grid, continue game
            PLAY(PLAYERS[0], GRID)
        else:
            break
        if GOLD_COIN in GRID:
            PLAY(PLAYERS[1], GRID)
        else:
            break

    RESTART = inputTextYN("Would you like to play again? (Yes/No) ")
    if RESTART.lower() == "yes":  # If input is 'Yes' game will restart.
        continue
    else:
        # Outputs thanks to players for playing.
        print("────────────────────────────────────────────────────────\n")
        print("Thank you {} & {} for playing Old Gold!".format(
            PLAYERS[0], PLAYERS[1]))
        print("\n────────────────────────────────────────────────────────")
        break
