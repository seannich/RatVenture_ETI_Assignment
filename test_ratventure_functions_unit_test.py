import pytest
from ratventure.ratventure_functions import *

#UTC15 - This test checks if the orb is spawned in any town except the first one.
def test_orbposition():
    
    townPosition = [1,12,22,26,53]
    value = spawnorb(townPosition)
    assert value == townPosition
    assert value != 1