import pytest
from ratventure.ratventure_functions import *


def test_mainMenuUI():
    value = mainMenuUI()
    assert value == "Welcome to Ratventure!\n----------------------\n1) New Game\n2) Resume Game\n3) Exit Game"

def test_mainMenu(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 1)
    value = mainMenu()
    assert value == 1

def test_townMenuUI():
    value = mainMenuUI()
    assert value == "Enter choice: 1\nDay 1: You are in a town.\n1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game\nEnter choice:"

def test_townMenu(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 1)
    value = mainMenu()
    assert value == 1
