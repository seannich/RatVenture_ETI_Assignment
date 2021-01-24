import pytest
from ratventure.ratventure_functions import *


#UTC11 - User inputs 1 in Outdoor Menu after escaping from combat
def test_outdoormenu_1():
    """
    This test tests if the user inputs "1" into the Outdoor Menu after escaping from combat (i.e. Run function in Combat Menu)
    Expected outcome is player's combat = true
    """
    player = Player()
    outdoorMenuinput(1,player)

    assert player.combat == True

#UTC12 - User inputs 2 in Outdoor Menu after escaping from combat
def test_outdoormenu_2():
    """
    This test tests if the user inputs "2" into the Outdoor Menu after escaping from combat (i.e. Run function in Combat Menu)
    Expected outcome is player's combat = true
    """
    player = Player()
    outdoorMenuinput(2,player)

    assert player.combat == True

#UTC13 - User inputs 3 in Outdoor Menu after escaping from combat
def test_outdoormenu_3():
    """
    This test tests if the user inputs "3" into the Outdoor Menu after escaping from combat (i.e. Run function in Combat Menu)
    Expected outcome is player's combat = false
    """
    player = Player()
    outdoorMenuinput(3,player)

    assert player.combat == False

#UTC14 - User inputs 4 in Outdoor Menu after escaping from combat
def test_outdoormenu_4():
    """
    This test tests if the user inputs "4" into the Outdoor Menu after escaping from combat (i.e. Run function in Combat Menu)
    Expected outcome is player's combat = false
    """
    player = Player()
    outdoorMenuinput(4,player)

    assert player.combat == False