import os
#Player class for when the player first starts the game
class Player:
    def __init__(self):
        Player.name = 'The Hero'
        Player.damage = '2-4'
        Player.minDamage = 2
        Player.maxDamage = 4
        Player.defence = 1
        Player.hp = 20
        Player.day = 1
        #self.positionX = 0  delete if unneeded 
        #self.positionY = 0  delete if unneeded 
        Player.location = 'You are in a Town'
        Player.locationTag = 'H'

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

def townMenuUI():
    """
    
    Day 1: You are in a town.
    1) View Character
    2) View Map
    3) Move
    4) Rest
    5) Save Game
    6) Exit Game

    """
    townmenuUI = "Day 1: You are in a town.\n1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game"
    print(townmenuUI)

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

def outdoorMenuUI():
    """
    
    1) View Character
    2) View Map
    3) Move
    4) Exit Game

    """
    outdoorMenuUI = "1) View Character\n2) View Map\n3) Move\n4) Exit Game"
    print(outdoorMenuUI)

    return outdoorMenuUI

def outdoorMenu():
    """
    takes in and displays player input choice
    """
    choice = int(input("Enter choice: "))
    if choice > 4 or choice < 0 :
        print("Invalid number. Please try again.")
        return "Invalid number. Please try again."
    else:
        return choice
"""
    "You deal" + damage "to the Rat"
    "Ouch! The Rat hit you for" + damage "!"
    "You have" + hp + "HP left."
    "Encounter! - Rat"
    "Damage:" + damage
    "Defence:" + defence
    "HP:" + hp
"""
def attackMenuUI(): #N

    """
    1) Attack
    2) Run
    """

    attackMenuUI = "1) Attack\n2) Run"
    print(attackMenuUI)

    return attackMenuUI

def attackMenu():
    """
    takes in and displays player input choice
    """
    choice = int(input("Enter choice: "))
    if choice > 2 or choice < 0 :
        print("Invalid number. Please try again.")
        return "Invalid number. Please try again."
    else:
        return choice
import sys
import pickle

"""
def main():

choice ='0'
while choice =='0':
    print("Welcome to Ratventure!")
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Rest")
    print("5) Save Game")
    print("6) Exit Game")


    choice = input ("Enter choice: ")
    if choice == "1":
        print("Enter choice: 1") #Display stats
        print("The Hero")
        print(" Damage:" + damage)
        print("Defence:" + defence)
        print("     HP:" + hp)

    elif choice == "2": 
        print("Enter choice: 2") #Display map
        print("+---+---+---+---+---+---+---+---+ \
               |H/T|   |   |   |   |   |   |   | \
               +---+---+---+---+---+---+---+---+ \
               |   |   |   | T |   |   |   |   | \
               +---+---+---+---+---+---+---+---+ \
               |   |   |   |   |   | T |   |   | \
               +---+---+---+---+---+---+---+---+ \
               |   | T |   |   |   |   |   |   | \
               +---+---+---+---+---+---+---+---+ \
               |   |   |   |   |   |   |   |   | \
               +---+---+---+---+---+---+---+---+ \
               |   |   |   |   |   |   |   |   | \
               +---+---+---+---+---+---+---+---+ \
               |   |   |   |   | T |   |   |   | \
               +---+---+---+---+---+---+---+---+ \
               |   |   |   |   |   |   |   | K | \
               +---+---+---+---+---+---+---+---+")  #-> x axis
    elif choice == "3": #Move
    print("Enter choice: 3")
    print("W = up; A = left; S = down; D = right")

    elif choice == "4":     
    print("Enter choice: 4")
    self.hp == 20
    print("You are fully healed.")
    elif choice == "5":
    print("Enter choice: 5")
    data = {'health':100, 'gold': 1560, 'name': 'mariano'}
    print("Game saved.")
    elif choice == "6":
    print("Enter choice: 6")
    sys.exit(0)
    else:
        print("Please choose a number from 1 to 6.")

 def second_menu():
     print("This is the second menu")

 main()


#load save file
 #with open('savefile', 'w') as f:
    #pickle.dump(data, f)

#with open('savefile') as f:
    #data = pickle.load(f)

"""
"""
    map = ("+---+---+---+---+---+---+---+---+ \
            | T |   |   |   |   |   |   |   | \
            +---+---+---+---+---+---+---+---+ \
            |   |   |   | T |   |   |   |   | \
            +---+---+---+---+---+---+---+---+ \
            |   |   |   |   |   | T |   |   | \
            +---+---+---+---+---+---+---+---+ \
            |   | T |   |   |   |   |   |   | \
            +---+---+---+---+---+---+---+---+ \
            |   |   |   |   |   |   |   |   | \
            +---+---+---+---+---+---+---+---+ \
            |   |   |   |   |   |   |   |   | \
            +---+---+---+---+---+---+---+---+ \
            |   |   |   |   | T |   |   |   | \
            +---+---+---+---+---+---+---+---+ \
            |   |   |   |   |   |   |   | K | \
            +---+---+---+---+---+---+---+---+")  #-> x axis
"""
def mapUI():
    """
    Function to create map UI
    """

    map = "+---+---+---+---+---+---+---+---+\n"
    for x in range(1,65):
        if (x % 8) == 0 and x != 64:
            map += "|   |\n+---+---+---+---+---+---+---+---+\n"
        elif x == 1 or x == 12 or x == 22 or x == 26 or x == 53:
            map += "| T "
        elif x == 64:
            map += "| K |\n+---+---+---+---+---+---+---+---+\n"
        else:
            map += "|   "
    
    print(map)
    return(map)


