import pytest
from ratventure.ratventure_functions import *

#UTC 16 - The test checks if the player is holding orb of power ans his stats have been increased by 5.

def test_playerhasorb():
    player = Player()

    obtainOrb(player)

    assert player.hasOrb == True
    assert player.maxDamage == 9
    assert player.minDamage == 7
    assert player.defence == 6
