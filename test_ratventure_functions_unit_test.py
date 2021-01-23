import pytest
from ratventure.ratventure_functions import *

#UTC07- Run from Rat
def test_player_run1():
    """
    This test follows the scenario where the opponent is a rat.
    This test tests if the player is successfully out of combat and the opponent's HP restored to full.
    Expected outcome for rat hp is 10 and player's combat = false
    """
    player = Player()
    rat = Enemy("Rat", 1, 3, 1, 10)

    player.combat = True
    run(player,rat) 

    assert player.combat == False
    assert rat.hp == 10

#UTC08- Run from Rat King
def test_player_run2():
    """
    This test follows the scenario where the opponent is the Rat King.
    This test tests if the player is successfully out of combat and the opponent's HP restored to full.
    Expected outcome for Rat King's hp is 25 and player's combat = false
    """
    player = Player()
    ratk = Enemy("Rat King", 8, 12, 5, 25)

    player.combat = True
    run(player,ratk) 

    assert player.combat == False
    assert ratk.hp == 25