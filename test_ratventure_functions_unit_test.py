import pytest
from ratventure.ratventure_functions import *

# UTC01 - Attack
def test_player_attack_2dmg():
    """
    This test takes the scenario that the player deals 2 damage to the rat. Rat will deal 1 damage by default

    Expected output for rat hp is 9
    """
    player = Player()
    rat = Enemy("Rat", 1, 3, 1, 10)

    dealDamage(player, 2, rat, 1)
    
    assert rat.hp == 9

# UTC02 - Attack
def test_player_attack_3dmg():
    """
    This test takes the scenario that the player deals 3 damage to the rat. Rat will deal 1 damage by default

    Expected output for rat hp is 8
    """
    player = Player()
    rat = Enemy("Rat", 1, 3, 1, 10)

    dealDamage(player, 3, rat, 1)
    
    assert rat.hp == 8

# UTC03 - Attack
def test_player_attack_4dmg():
    """
    This test takes the scenario that the player deals 4 damage to the rat. Rat will deal 1 damage by default

    Expected output for rat hp is 3
    """
    player = Player()
    rat = Enemy("Rat", 1, 3, 1, 10)

    dealDamage(player, 4, rat, 1)
    
    assert rat.hp == 7

# UTC04 - Attack
def test_rat_attack_1dmg():
    """
    This test takes the scenario that the rat deals 1 damage to the player. Player will deal 2 damage by default

    Expected output for player hp is 20
    """
    player = Player()
    rat = Enemy("Rat", 1, 3, 1, 10)

    dealDamage(player, 2, rat, 1)
    
    assert player.hp == 20

# UTC05 - Attack
def test_rat_attack_2dmg():
    """
    This test takes the scenario that the rat deals 2 damage to the player. Player will deal 2 damage by default

    Expected output for player hp is 20
    """
    player = Player()
    rat = Enemy("Rat", 1, 3, 1, 10)

    dealDamage(player, 2, rat, 2)
    
    assert player.hp == 19
    
# UTC06 - Attack
def test_rat_attack_3dmg():
    """
    This test takes the scenario that the rat deals 3 damage to the player. Player will deal 2 damage by default

    Expected output for player hp is 18
    """
    player = Player()
    rat = Enemy("Rat", 1, 3, 1, 10)

    dealDamage(player, 2, rat, 3)
    
    assert player.hp == 18

# UTC09 - Attack
def test_player_died():
    '''
    This test takes the scenario that player's hp is 0 or below

    Expected output for player.alive is false
    '''
    player = Player()
    rat = Enemy("Rat", 1, 3, 1, 10)
    player.hp = 0

    dealDamage(player, 2, rat, 3)

    assert player.alive == False

# UTC10 - Attack
def test_player_won():
    '''
    This test takes the scenario that enemy's hp is 0 or below

    Expected output for player.combat is false
    '''
    player = Player()
    rat = Enemy("Rat", 1, 3, 1, 10)
    rat.hp = 0

    dealDamage(player, 2, rat, 3)

    assert player.combat == False
