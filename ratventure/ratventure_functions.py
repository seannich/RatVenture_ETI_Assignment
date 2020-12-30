import os
import sys
import pickle

class Player:
    """
    Player class for when the player first starts the game
    """
    def __init__(self):
        self.name = 'The Hero'
        self.damage = '2-4'
        self.minDamage = 2
        self.maxDamage = 4
        self.defence = 1
        self.hp = 20
        self.day = 1
        self.position = 1
        self.location = 'You are in a Town'
        self.locationTag = 'H'
 
player = Player()

def mapUI(position):
    """
    Displays UI for map

    +---+---+---+---+---+---+---+---+ 
    | T |   |   |   |   |   |   |   | 
    +---+---+---+---+---+---+---+---+ 
    |   |   |   | T |   |   |   |   | 
    +---+---+---+---+---+---+---+---+ 
    |   |   |   |   |   | T |   |   | 
    +---+---+---+---+---+---+---+---+ 
    |   | T |   |   |   |   |   |   | 
    +---+---+---+---+---+---+---+---+ 
    |   |   |   |   |   |   |   |   | 
    +---+---+---+---+---+---+---+---+ 
    |   |   |   |   |   |   |   |   | 
    +---+---+---+---+---+---+---+---+ 
    |   |   |   |   | T |   |   |   | 
    +---+---+---+---+---+---+---+---+ 
    |   |   |   |   |   |   |   | K | 
    +---+---+---+---+---+---+---+---+
    """

    map = "+---+---+---+---+---+---+---+---+\n"
    townPosition = [1,12,22,26,53]

    for x in range(1,65):
        if (x % 8) == 0 and x != 64:
            map += "|   |\n+---+---+---+---+---+---+---+---+\n"
        elif x in townPosition:
            if x == position:
                map += "|H/T"
            else:
                map += "| T "
        elif x == 64:
            if x == position:
                map += "|H/K|\n+---+---+---+---+---+---+---+---+\n"
            else:
                map += "| K |\n+---+---+---+---+---+---+---+---+\n"
        elif x == position and x != townPosition and x != 64:
            map += "| H "
        else:
            map += "|   "
    
    print(map)
    return(map)

def playerMovement():
    """
    This function shows the map UI and allows player to move their character.
    Player postion starts at 1.
    
    W: player.postion -8
    A: player.postion -1
    S: player.postion +8
    D: player.postion +1

    If player goes outside of map: How about we explore the area ahead of us later.

    If player chooses something other than wasd: Please select a valid option.

    If player chooses acceptable choice: return player postition

    """
    position = player.position

    topWall = [1,2,3,4,5,6,7,8]
    leftWall = [1,9,17,25,33,41,49,57]
    bottomWall = [57,58,59,60,61,62,63,64]
    rightWall = [8,16,24,32,40,48,56,64]
    posibleChoice = ["w", "a", "s", "d"]

    errorMsg = "How about we explore the area ahead of us later."
    invalidChoice = "Please select a valid option."

    invalidMovement = True

    while invalidMovement:
        mapUI(position)
        print("W = up; A = left; S = down; D = right")
        choice = input("Your move: ")

        if choice not in posibleChoice:
            print(invalidChoice)
            return invalidChoice
        else:
            if choice == "w":
                if position in topWall:
                    print(errorMsg)
                else:
                    position -= 8
                    invalidMovement = False
                    player.position = position
                    mapUI(player.position)
    
            if choice == "a":
                if position in leftWall:
                    print(errorMsg)
                else:
                    position -= 1
                    invalidMovement = False
                    player.position = position
                    mapUI(player.position)

            if choice == "s":
                if position in bottomWall:
                    print(errorMsg)
                else:
                    position += 8
                    invalidMovement = False
                    player.position = position
                    mapUI(player.position)

            if choice == "d":
                if position in rightWall:
                    print(errorMsg)
                else:
                    position += 1
                    invalidMovement = False
                    player.position = position
                    mapUI(player.position)

            if invalidMovement :
                return errorMsg
            else:
                return player.position
    
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
    Displays UI for town menu

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
    Displays UI for outdoor menu

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
def attackMenuUI():
    """
    Displays UI for town menu

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

