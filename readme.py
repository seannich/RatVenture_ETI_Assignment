# created repo

"""
USER STORIES
=========================================================================================================================================================================================
NO.     FEATURE                         SUB FEATURE             USER STORY
1       UI Creation                     Main Menu               As a player I want to be able to select an option so that I can start the game.
                                                                As a player I want to be able to select an option so that I can resume a saved game.
                                                                As a player I want to be able to select an option so that I can exit the game.

                                        Various Game Menus      As a player I want to have different game menus so that I can do different activities.
                                                                As a player I want to be able to have combat options so that I can fight my enemies.

                                        World Map               As a player I want to be able to see a world map so that I know where my character is.

2       Functions Creation in Town      View Character          As a player I want to be able to view my character’s damage so that I know how much damage I deal to enemies.
                                                                As a player I want to be able to view my character’s defence so that I know how well I defend against enemies.
                                                                As a player I want to be able to view my character’s health so that I know when I’m supposed to heal myself.

                                        View Map                As a player I want to be able to view my character on the map so that I can plan out my next move.

                                        Move                    As a player I want to be able to leave the town so that I can progress to the end.

                                        Rest                    As a player I want to be able to rest so that I can restore my health.

3       Functions Creation for Combat   Attack                  As a player I want to be able to attack during a fight so that I can defeat the opponent.

                                        Run                     As a player I want to be able to run away from a fight so that I can prevent myself from dying if I am low on health.

4       Saving Player Progress          New Game                As a player I want to be able to start a new game so that I can play the game.

                                        Save Game               As a player I want to be able to save the game so that I can pause and come back to the game another time.

                                        Resume Game             As a player I want to load up a save of my previous game so that I can continue from where I stopped previously.

                                        Exit Game               As a player I want to be able to exit the game so that I can stop playing and come back another time.
#=========================================================================================================================================================================================

# METHODLOGOIES ADOPTED
# ==========================================
# NO.           MODEL
# 1             Iterative Model
# 2             Continuous Integration
# 3             DevOps
# 4             Agile
# ==========================================

# PRODUCT BACKLOG
# =====================================================================
# SPRINT NO.    TASKS               
# 1             UI Creation
#               1.  Create UI for world map
#               2.  Create main menu containing various choice numbers
#                   -New game
#                   -Resume game
#                   -Exit game
#               3.  Create various game menus with the respective choices
#                   -Town/Outdoor menu
#                   -Combat menu
#               Test to see if player input is displayed correctly
#               1.  Player choice is displayed correctly for various game menus

# 2             Create functions for town menu
#               1.  View character: 
#                   -Shows the player’s damage, defense, health
#               2.  View map: 
#                   -Shows world map
#               2.  Move: 
#                   -Shows the world map with instructions indicating which key moves the player in which direction. 
#                   -Displays the player’s chosen key.
#                   -Add 1 day to the time
#               2.  Rest: 
#                   -Shows the text “You are fully healed.”
#                   -Add 1 day to the time
#               Test if appropriate UI shows up and functions are working as intended
#               1.  View character: 
#                   -Shows the player’s stats properly. (eg. if player has 10hp it should be reflected there)
#               2.  View map: 
#                   -Shows the map with H being where the player currently is.
#               2.  Move: 
#                   -Shows the map and its instructions. The player’s chosen key is displayed properly. 
#                   -The position of H moves in the correct direction.
#                   -Ensure that 1 day is added to the time
#               2.  Rest: 
#                   -Rest text is shown
#                   --Player’s health is reset back to 20 
#                   -Ensure that 1 day is added to the time

# 3             Create functions for combat menu
#               1.  Attack:
#                   -Deal 2-4 damage to enemy
#                   -Display damage dealt to enemy
#                   -Damage dealt is calculated after deducting enemy defense from player’s attack
#                   -Display damage taken from enemy
#                   -Damage taken follows same calculation as damage dealt
#                   -Display remaining health
#                   -Display outdoor menu if enemy is defeated
#               2.  Run:
#                   -Displays outdoor menu
#               Update town menu into outdoor menu
#               1.  Display the following choices:
#                   -View character
#                   -View map
#                   -Move
#                   -Exit game
#               2.  If player ran, view character and view map brings player back into combat
#               3.  If brought into combat, enemy will recover all its health
#               Test combat menu
#               1.  Attack:
#                   -Damage is between 2-4
#                   -Damage dealt is displayed correctly
#                   -Player remaining health is displayed correctly
#                   -Enemy remaining health is displayed correctly
#                   -Outdoor menu is displayed after enemy is defeated
#               2.  Run:
#                   -Outdoor menu is displayed
#               Test outdoor menu
#               1.  The correct choices are shown
#               2.  If player ran, player is brought back into combat menu if view character or view map is chosen
#               3.  If brought back into combat, enemy has recovered all its health

# 4            Saving player progress
#               1.  New game:
#                   -New game is created with the player starting at the original position with full health.
#               2.  Save game:
#                   -Player progression is saved into .csv file
#                   -Overrides previous save file
#               3.  Resume game:
#                   -Game reads progress from existing .csv file
#               4.  Exit game:
#                   -Program stops running
#               Testing player saves
#               1.  New game:
#                   -Player should be at full health
#                   -Player should have no progress
#               2.  Save game: 
#                   -Player progress is written into a .csv file
#                   -.csv file is created if there is no existing one
#                   -Existing .csv file is overwritten
#               3.  Resume game:
#                   -Program successfully reads save file
#                   -Displays error message if unable to do so
#               4.  Exit game:
#                   -Program stops running successfully
# =====================================================================
#
#
"""