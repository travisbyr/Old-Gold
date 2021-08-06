"""
Project: Old Gold Game
Author:  Travis Byrman
School:  Waimea College
Date:    September 2018
Module:  Input.py
Purpose: User input functions, used throughout main.py
"""
def inputTextYN(prompt): #User can only input 'Yes' or 'No'
    while True:
        text = input(prompt)
        if "yes" in text.lower() or "no" in text.lower():
            return text
        else:
            print("Invalid input, please enter 'Yes' or 'No'")

def inputText(prompt): #If input is blank, ask same question
    while True:
        text = input(prompt)
        if " " in text or len(text) == 0:
            print("Invalid input, please enter some text")
        else:
            return text
            
def inputTextHelp(prompt): #If anything is entered continue
    while True:
        text = input(prompt)
        if len(text) == 0:
            return text
        
def inputNumber( prompt, lowest, highest ): #If input value is between minimum and maximum value, continue, else repeat question, tell user why input was rejected.
    while True:
        try:
            number = int(input(prompt))
            if number >= lowest and number <= highest: #Value must be entered between constant values
                return number
            else:
                raise ValueError
            
        except ValueError:
            print("Invalid input, please enter a value between {} and {}".format(lowest, highest))
            


