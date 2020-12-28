import pytest
import sys
import pickle

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
def map():
    map = ("+---+---+---+---+---+---+---+---+ \
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
    print(map)
    return(map)