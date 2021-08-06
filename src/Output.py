"""
Project: Old Gold Game
Author:  Travis Byrman
School:  Waimea College
Date:    September 2018
Module:  Output.py
Purpose: Functions that are used throughout main.py
"""

def INSTRUCTIONS(): #Instructions that can be printed if user chooses
        print("────────────────────────────────────────────────────────────────────────────────────────────────")
        print("                                   How to play!")
        print("The aim of the game is to be the first person to remove the gold coin '0'.")
        print("In order to move a coin there cannot be any silver coins 'O' to the left of it.")
        print("Coins can only be moved to the left and cannot jump over eachother. To remove a coin enter '1'")
        print("For the coin to be removed, it must be in the first square of the grid. To select")
        print("a coin to be moved, type the number that is under the coin that you want to select.")
        print("To move the coin, enter how many places you want the coin to move to the left.")
        print("─────────────────────────────────────────────────────────────────────────────────────────────────")
            
def BOX(List): #Boxes around items
    for i in range(len(List)):
        print("┌───┐", end = "")
    if(i == len(List)-1):
        print("", end = "\n")
    for i in range(len(List)):
        print("│{}│".format(List[i]), end = "")
    if(i == len(List)-1):
        print("", end = "\n") 
    for i in range(len(List)):
        print("└───┘" , end = "")
    if(i == len(List)-1):
        print("", end = "\n")
        
def NUMBER_LINE(List): #Number line for under boxes
    for i in range(1, len(List) + 1):
        if i < 10:    #For the first 9 boxes 
            print("  {}  ".format(i), end = "") #they get this
        else:
            print("  {} ".format(i), end = "")   #10+ boxes get this
        if(i == len(List) + 1 - 1):
            print("", end = "\n")
        