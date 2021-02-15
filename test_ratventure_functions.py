import pytest
import random
from ratventure.ratventure_functions import *

#Initialise player object for test
player = Player()

# TC01 - MAIN MENU ==================================
def test_mainMenuUI():
    """
    Input: None

    Output:
    Welcome to Ratventure!
    ----------------------
    1) New Game
    2) Resume Game
    3) Exit Game
    """
    value = mainMenuUI()
    assert value == "Welcome to Ratventure!\n----------------------\n1) New Game\n2) Resume Game\n3) Exit Game"

def test_mainMenu(monkeypatch):
    """
    Input: 1

    Output: 1 
    """
    monkeypatch.setattr("builtins.input", lambda _: 1)  
    value = mainMenu()
    assert value == 1


def test_mainMenu_invalid(monkeypatch):
    """
    Input: 8

    Output: Invalid number. Please try again.
    """
    monkeypatch.setattr("builtins.input", lambda _: 8)  
    value = mainMenu()
    assert value == "Invalid number. Please try again."

# TC02 - TOWN MENU ================================
def test_townMenuUI():
    """
    Input: None

    Output:
    Day 1: You are in a town.
    1) View Character
    2) View Map
    3) Move
    4) Rest
    5) Save Game
    6) Exit Game
    """
    value =townMenuUI()
    assert value == "Day 1: You are in a town.\n1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game"

def test_townMenu(monkeypatch):
    """
    Input: 1

    Output: 1 
    """
    monkeypatch.setattr("builtins.input", lambda _: 1)  
    value = townMenu()
    assert value == 1

def test_townMenu_invalid(monkeypatch):
    """
    Input: b

    Output: Invalid number. Please try again.
    """
    monkeypatch.setattr("builtins.input", lambda _: 9)  
    value = townMenu()
    assert value == "Invalid number. Please try again."

# TC - OUTDOOR MENU ================================
def test_outdoorMenuUI():
    """
    Input: None

    Output:
    1) View Character
    2) View Map
    3) Move
    4) Exit Game
    """
    value =outdoorMenuUI()
    assert value == "1) View Character\n2) View Map\n3) Move\n4) Exit Game"

def test_outdoorMenu(monkeypatch):
    """
    Input: 1

    Output: 1 
    """    
    monkeypatch.setattr("builtins.input", lambda _: 1)  
    value = outdoorMenu()
    assert value == 1

def test_outdoorMenu_invalid(monkeypatch):
    """
    Input: 6

    Output: Invalid number. Please try again.
    """
    monkeypatch.setattr("builtins.input", lambda _: 6)  
    value = attackMenu(player)
    assert value == "Invalid number. Please try again."

# TC - ATTACK MENU =================================
def test_attackMenuUI():
    """
    1) Attack
    2) Run
    """
    value =attackMenuUI()
    assert value == "1) Attack\n2) Run"

def test_attackMenu(monkeypatch):
    """
    Input: 1

    Output: 1 
    """    
    monkeypatch.setattr("builtins.input", lambda _: 1)  
    value = attackMenu(player)
    assert value == 1

def test_attackMenu_error(monkeypatch):
    """
    Input: 6

    Output: Invalid number. Please try again.
    """
    monkeypatch.setattr("builtins.input", lambda _: 6)  
    value = attackMenu(player)
    assert value == "Invalid number. Please try again."
 
# TC - Hero Statistic 
def test_herostats():
    ''' 
    enter choice: 1
    This function prints out the player's name, damage, defence and HP.
    Expected Output: 
    The Hero
    Damage: 2-4
    Defence: 1
    HP: 20
    '''
    value = player.herostats()
    assert value == "The Hero\nDamage: 2-4\nDefence: 1\nHP: 20"

# TC -  Hero Rest 
def test_herorest():
    '''
    enter choice:4
    This function restores the player to 20, adds 1 day to the day count and prints out "You are fully healed".
    Expected Output:
    (20, 2)
    '''
    value = player.herorest()
    assert value == (20, 2)


# SPRINT 2 
# TC - PLAYERMOVEMENT 
def test_playerMovement_oob(monkeypatch):
    """
    This function shows the map UI and allows player to move their character.
    Player postion starts at 1.

    If player goes outside of map: How about we explore the area ahead of us later.

    """
    monkeypatch.setattr("builtins.input", lambda _: 'w')  
    value = player.playerMovement()
    assert value == "How about we explore the area ahead of us later."

def test_playerMovement_invalid(monkeypatch):
    """
    This function shows the map UI and allows player to move their character.
    Player postion starts at 1.

    If player chooses something other than wasd: Please select a valid option.

    """
    monkeypatch.setattr("builtins.input", lambda _: 'Q')  
    value = player.playerMovement()
    assert value == "Please select a valid option."

def test_playerMovement(monkeypatch):
    """
    This function shows the map UI and allows player to move their character.
    Player postion starts at 1.

    If player chooses acceptable choice: return player postition

    """
    monkeypatch.setattr("builtins.input", lambda _: 'd')  
    value = player.playerMovement()
    assert value == 2

# SPRINT 3
# TC_36
def test_player_runFromEnemy(monkeypatch):
    '''
    This function is to test if the player runs from the enemy.
    '''
    monkeypatch.setattr("builtins.input", lambda _: 2)
    value = attackMenu(player)
    assert value == "You run and hide."

# TC_37
def test_player_runFromEnemy_error(monkeypatch):
    '''
    Input: 6
    Output: Invalid Number. Please try again.
    '''
    monkeypatch.setattr("builtins.input", lambda _: 6)
    value = attackMenu(player)
    assert value == "Invalid number. Please try again."

# TC_41
def test_mapUI(monkeypatch):
    """
    This functions shows the world map and displays the towns and where the Orb of Power is.
    """
    value = mapUI(player)
    if (mapUI(player) == "+---+---+---+---+---+---+---+---+| T |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |T/O|   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   | T |   |   |+---+---+---+---+---+---+---+---+|   | T |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   | T |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   | K |+---+---+---+---+---+---+---+---+"):
        assert value == "+---+---+---+---+---+---+---+---+| T |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |T/O|   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   | T |   |   |+---+---+---+---+---+---+---+---+|   | T |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   | T |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   | K |+---+---+---+---+---+---+---+---+"
    elif (mapUI(player) == "+---+---+---+---+---+---+---+---+| T |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   | T |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |T/O|   |   |+---+---+---+---+---+---+---+---+|   | T |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   | T |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   | K |+---+---+---+---+---+---+---+---+"):
        assert value == "+---+---+---+---+---+---+---+---+| T |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   | T |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |T/O|   |   |+---+---+---+---+---+---+---+---+|   | T |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   | T |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   | K |+---+---+---+---+---+---+---+---+"
    elif (mapUI(player) == "+---+---+---+---+---+---+---+---+| T |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   | T |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   | T |   |   |+---+---+---+---+---+---+---+---+|   |T/O|   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   | T |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   | K |+---+---+---+---+---+---+---+---+"):
        assert value == "+---+---+---+---+---+---+---+---+| T |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   | T |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   | T |   |   |+---+---+---+---+---+---+---+---+|   |T/O|   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   | T |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   | K |+---+---+---+---+---+---+---+---+"
    elif (mapUI(player) == "+---+---+---+---+---+---+---+---+| T |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   | T |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   | T |   |   |+---+---+---+---+---+---+---+---+|   | T |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |T/O|   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   | K |+---+---+---+---+---+---+---+---+"):
        assert value == "+---+---+---+---+---+---+---+---+| T |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   | T |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   | T |   |   |+---+---+---+---+---+---+---+---+|   | T |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |T/O|   |   |   |+---+---+---+---+---+---+---+---+|   |   |   |   |   |   |   | K |+---+---+---+---+---+---+---+---+"
    
