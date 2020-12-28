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
    choice = int(input("Enter choice: "))
    if choice > 3 or choice < 0 :
        print("Invalid number. Please try again.")
        return "Invalid number. Please try again."
    else:
        return choice

def townMenuUI(): #N
    """
    
    Day 1: You are in a town.
    1) View Character
    2) View Map
    3) Move
    4) Rest
    5) Save Game
    6) Exit Game

    """
    os.system('cls')
    townmenuUI = "Day 1: You are in a town.\n1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game"
    print(townmenuUI)

        #townMenu()
    return townmenuUI

def townMenu():
    """
    takes in and displays player input choice
    """
    choice = int(input("Enter choice: "))
    if choice > 6 or choice < 0 :
        print("Invalid number. Please try again.")
        return "Invalid number. Please try again."
    else:
        return choice

def outdoorMenuUI(): #N
    """
    
    1) View Character
    2) View Map
    3) Move
    4) Exit Game

    """
    os.system('cls')
    outdoorMenuUI = "1) View Character\n2) View Map\n3) Move\n4) Exit Game"
    print(outdoorMenuUI)

        #outdoorMenu()
    return outdoorMenuUI

def outdoorMenu():
    """
    takes in and displays player input choice
    """
    choice = input("Enter choice: ")
    return choice


def attackMenuUI(): #N
 
    "You deal" + damage "to the Rat"
    "Ouch! The Rat hit you for" + damage "!"
    "You have" + hp + "HP left."
    "Encounter! - Rat"
    "Damage:" + damage
    "Defence:" + defence
    "HP:" + hp
    "1) Attack"
    "2) Run""


    os.system('cls')
    attackMenuUI = "1) View Character\n2) View Map\n3) Move\n4) Exit Game"
    print(attackMenuUI)

        #attackMenu()
    return attackMenuUI

def attackMenu():
    """
    takes in and displays player input choice
    """
    choice = input("Enter choice: ")
    return choice

def runMenuUI(): #N
 """
    You run and hide.
    1) View Character
    2) View Map
    3) Move
    4) Exit Game
"""

    os.system('cls')
    runMenuUI = " You run and hide.\n1) View Character\n2) View Map\n3) Move\n4) Exit Game"
    print(runMenuUI)

        #runMenu()
    return runMenuUI

def runMenu():
    """
    takes in and displays player input choice
    """
    choice = input("Enter choice: ")
    return choice
    
