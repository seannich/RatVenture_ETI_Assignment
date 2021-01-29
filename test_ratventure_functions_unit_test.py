import pytest
from ratventure.ratventure_functions import *

# UTC16
def test_rat_king_object():
    '''
    This function is to test if the Rat King object is created / initialised as intended to.
    '''
    ratKing = createRatKing()

    assert ratKing.name == "Rat King"
    assert ratKing.minDamage == 8
    assert ratKing.maxDamage == 12
    assert ratKing.defence == 5
    assert ratKing.maxHp == 25
    assert ratKing.alive == True

