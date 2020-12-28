import os

def mainMenuUI():
    """
    Displays UI for main menu

    Welcome to Ratventure!
    ----------------------
    1) New Game
    2) Resume Game
    3) Exit Game

    """
    os.system('cls')
    menuUI = "Welcome to Ratventure!\n----------------------\n1) New Game\n2) Resume Game\n3) Exit Game"
    print(menuUI)

    #mainMenu()
    return menuUI

def mainMenu():
    """
    takes in and displays player input choice
    """
    choice = input("Enter choice: ")
    return choice