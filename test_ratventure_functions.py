import pytest
from ratventure.ratventure_functions import *

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

# test town menu invalid number

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

def test_outdoorMenu_error(monkeypatch):
    """
    Input: 6

    Output: Invalid number. Please try again.
    """
    monkeypatch.setattr("builtins.input", lambda _: 6)  
    value = attackMenu()
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
    value = attackMenu()
    assert value == 1

def test_attackMenu_error(monkeypatch):
    """
    Input: 6

    Output: Invalid number. Please try again.
    """
    monkeypatch.setattr("builtins.input", lambda _: 6)  
    value = attackMenu()
    assert value == "Invalid number. Please try again."

# TC - TOWN MAP
def test_mapUI():
    """
    Input: None

    Output:
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
    value = mapUI()
    assert value == "+---+---+---+---+---+---+---+---+\n| T |   |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+---+\n|   |   |   | T |   |   |   |   |\n+---+---+---+---+---+---+---+---+\n|   |   |   |   |   | T |   |   |\n+---+---+---+---+---+---+---+---+\n|   | T |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+---+\n|   |   |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+---+\n|   |   |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+---+\n|   |   |   |   | T |   |   |   |\n+---+---+---+---+---+---+---+---+\n|   |   |   |   |   |   |   | K |\n+---+---+---+---+---+---+---+---+\n"

# TC - Hero Statistic 
def test_herostats(monkeypatch):
    ''' 
    enter choice: 1
    This function prints out the player's name, damage, defence and HP.
    Expected Output: 
    The Hero
    Damage: 2-4
    Defence: 1
    HP: 20
    '''
    monkeypatch.setattr("builtins.input", lambda _: 1)  
    value = herostats()
    assert value == "The Hero\nDamage: 2-4\nDefence: 1\nHP: 20"

# TC -  Hero Rest 
def test_herorest(monkeypatch):
    '''
    enter choice:4
    This function restores the player to 20, adds 1 day to the day count and prints out "You are fully healed".
    Expected Output:
    (20, 2)
    '''
    monkeypatch.setattr("builtins.input", lambda _: 4)  
    value = herorest()
    assert value == (20, 2)
