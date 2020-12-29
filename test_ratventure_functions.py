import pytest
from ratventure.ratventure_functions import *

# TC01 - MAIN MENU ==================================
def test_mainMenuUI():
    """
    Displays UI for main menu

    Welcome to Ratventure!
    ----------------------
    1) New Game
    2) Resume Game
    3) Exit Game
    """
    value = mainMenuUI()
    assert value == "Welcome to Ratventure!\n----------------------\n1) New Game\n2) Resume Game\n3) Exit Game"

def test_mainMenu(monkeypatch):
    #input 1 
    monkeypatch.setattr("builtins.input", lambda _: 1)  
    value = mainMenu()
    assert value == 1

# TC02 - TOWN MENU ================================
def test_townMenuUI():
    value =townMenuUI()
    assert value == "Day 1: You are in a town.\n1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game"

def test_townMenu(monkeypatch):
    #input 2
    monkeypatch.setattr("builtins.input", lambda _: 1)  
    value = townMenu()
    assert value == 1


# TC - OUTDOOR MENU ================================
def test_outdoorMenuUI():
    value =outdoorMenuUI()
    assert value == "1) View Character\n2) View Map\n3) Move\n4) Exit Game"

def test_outdoorMenu(monkeypatch):
    #input 2
    monkeypatch.setattr("builtins.input", lambda _: 1)  
    value = outdoorMenu()
    assert value == 1

def test_outdoorMenu_error(monkeypatch):
    #input 6 - should display error message
    monkeypatch.setattr("builtins.input", lambda _: 6)  
    value = attackMenu()
    assert value == "Invalid number. Please try again."

# TC - ATTACK MENU =================================
def test_attackMenuUI():
    value =attackMenuUI()
    assert value == "1) Attack\n2) Run"

def test_attackMenu(monkeypatch):
    #input 2
    monkeypatch.setattr("builtins.input", lambda _: 1)  
    value = attackMenu()
    assert value == 1

def test_attackMenu_error(monkeypatch):
    #input 6 - should display error message
    monkeypatch.setattr("builtins.input", lambda _: 6)  
    value = attackMenu()
    assert value == "Invalid number. Please try again."
from ratventure.ratventure_functions import * 

# TC - TOWN MAP
def test_mapUI():
    """
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
