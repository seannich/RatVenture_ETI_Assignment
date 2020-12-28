import pytest
from ratventure.ratventure_functions import *


def test_mainMenuUI():
    value = mainMenuUI()
    assert value == "Welcome to Ratventure!\n----------------------\n1) New Game\n2) Resume Game\n3) Exit Game"

def test_mainMenu(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 1)
    value = mainMenu()
    assert value == 1
