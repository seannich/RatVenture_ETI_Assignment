# RatVenture


## USER STORIES
|      NO.      |    FEATURE    |  SUB FEATURE  |   USER STORY  |
| ------------- | ------------- | ------------- | ------------- |
|1|UI Creation|Main Menu|As a player I want to be able to select an option so that I can start the game.|
|    |    |    | As a player I want to be able to select an option so that I can resume a saved game.|
|    |    |    | As a player I want to be able to select an option so that I can exit the game.|
|    |    |Various Game Menus|As a player I want to have different game menus so that I can do different activities.|
|    |    |    |As a player I want to be able to have combat options so that I can fight my enemies.|
|    |    |World Map|As a player I want to be able to see a world map so that I know where my character is.| 
|2|Functions Creation in Town|View Character|As a player I want to be able to view my character’s damage so that I know how much damage I deal to enemies.|
|    |    |    |As a player I want to be able to view my character’s defence so that I know how well I defend against enemies.|
|    |    |    |As a player I want to be able to view my character’s health so that I know when I’m supposed to heal myself.|
|    |    |View Map|As a player I want to be able to view my character on the map so that I can plan out my next move.|
|    |    |Move |As a player I want to be able to leave the town so that I can progress to the end.|
|    |    |Rest|As a player I want to be able to rest so that I can restore my health.|
|3|Functions Creation for Combat|Attack|As a player I want to be able to attack during a fight so that I can defeat the opponent.|
|    |    |Run|As a player I want to be able to run away from a fight so that I can prevent myself from dying if I am low on health.|
|4|Saving Player Progress|New Game|As a player I want to be able to start a new game so that I can play the game.|
|    |    |Save Game|As a player I want to be able to save the game so that I can pause and come back to the game another time.|
|    |    |Resume Game|As a player I want to load up a save of my previous game so that I can continue from where I stopped previously.|
|    |    |Exit Game|As a player I want to be able to exit the game so that I can stop playing and come back another time.|


## METHODLOGOIES CONSIDERED

1. Iterative 
  - Considerations:
    - When the requirements of the complete system are clearly defined and understood.
    - The major requirements are defined, while some functionalities and requested enhancements evolve with the process of the development process.
    - A new technology is being used and is being learnt by the development team, while they are working on the project.
  
In this assignment, all the requirements of the final product are clearly defined and understood. The timeline of the different development stages have been planned out in the Sprint Log. Each sprint we release a specific set of usable features, which are enhanced in the next sprint by other features. The features will be more advanced as each sprint passes, for example the first sprint will be simply creating the UI of the various game menus. The following sprints will be the actual development of the game functions such as Move, Rest and so on. As the Iterative Model allows accessing previous phases, we will be able to access the code from the previous sprints if any changes have to be made to the existing features. We will also be using a new technology, PyTest, to run the automated tests.

2. Agile 
  - Considerations:
    - Agile model used in the following scenarios:
    - Few lenient processes in place and few initial product & regulatory requirements 
    - Having a flexible approach towards software development. Priorities and requirements can be easily adjusted during the project to meet the requirements of the stakeholders.
 
Agile model allows the development to be incremental and iterative, having time in sprint to take place each 1 to 3 weeks each sprint being set in github as milestones. This model promotes a disciplined project management process that encourages inspections and adaptations frequently, the systematic process of Planning, implementing, building and testing. Additionally this model provides more value to the work of the development team, providing them more time to develop the application by reducing those non-productive issues. The QA will be able to track the project status with greater awareness, being able to catch and address the issues or bugs quickly by creating it on the github kaman board which will notify the developers on the issues and resolve it as soon as possible. 
          
3. Waterfall
A linear project management approach, where stakeholders and requirements are gathered at the beginning of the project. A sequential approach is planned out to accommodate the requirements. This method is named so that each phrase of the project cascades into the next.

  - Advantages: 
    - It is a thorough, structured methodology suitable for smaller projects with deliverables that are easy to define. Going through these steps (Shown in figure above) 
    - Waterfall relies on the team to follow a sequence of steps, only moving when the previous phase has been completed.
    - Able to determine the end goal early 	
    - Unlike scrum (Dividing projects into sprints), this method set the end goal as their main focus and has a concrete scheduling of the end date, this eliminates the risk of slowing down or pausing during the process. 
    - Transfer information well
    - Waterfall approach is highly methodical, it provides a clean transfer of information for each step. This methodology prioritizes accessible information so new additions to the team can get up to speed quickly if required. 

  - Disadvantages:
    - Changes towards the projects are challenging 
    - Waterfall follows a strict set of steps, in the traditional waterfall there is no room for unexpected changes or revisions. To be able to change the parameters of the project, it could render much of the work that will throw of the entire timeline
    - Excludes the end user 
    - This methodology focuses little on the end user involved in the project. 
    - Delay testing until after completion of the project
    - Teams have to follow the process of the methodology and wait until the step (testing) to be able to start their trial and error phrase. At this point the project might have taken a considerable time to complete, hence should there be an error that requires a large amount of revision, it can cause severe delays to the project.
    
For this assignment, all our requirements are well defined and will not change. We started off the assignment by carrying out requirement gathering and documentation. We have also planned out the development schedule with specific end goals in mind, hence reducing time wastage. We will also implement automated testing only after our features have been completed.
      
4. TBA

## PRODUCT BACKLOG

|SPRINT NO.|TASKS|         
| ------------- | ------------- |
|1|UI Creation|
| |1.  Create UI for world map|
| |2.  Create main menu containing various choice numbers
| | -New game|
| | -Resume game|
| | -Exit game|
| |3.  Create various game menus with the respective choices|
| | -Town/Outdoor menu|
| | -Combat menu|
| |Test to see if player input is displayed correctly|
| |1.  Player choice is displayed correctly for various game menus|
|2|Create functions for town menu|
| |1.  View character:|
| | -Shows the player’s damage, defense, health|
| |2.  View map:|
| | -Shows world map|
| |3.  Move:|
| | -Shows the world map with instructions indicating which key moves the player in which direction.|
| |-Displays the player’s chosen key.|
| |-Add 1 day to the time|
| |4.  Rest:|
| |-Shows the text “You are fully healed.”|
| |-Add 1 day to the time|
| |Test if appropriate UI shows up and functions are working as intended|
| |1.  View character:|
| | -Shows the player’s stats properly. (eg. if player has 10hp it should be reflected there)|
| |2.  View map:|
| | -Shows the map with H being where the player currently is.|
| |3.  Move:|
| | -Shows the map and its instructions. The player’s chosen key is displayed properly.|
| | -The position of H moves in the correct direction.|
| | -Ensure that 1 day is added to the time|
| |4.  Rest:|
| | -Rest text is shown|
| | -Player’s health is reset back to 20 |
| | -Ensure that 1 day is added to the time|
|3|Create functions for combat menu|
| |1.  Attack:|
| | -Deal 2-4 damage to enemy|
| | -Display damage dealt to enemy|
| | -Damage dealt is calculated after deducting enemy defense from player’s attack||
| | -Display damage taken from enemy|
| | -Damage taken follows same calculation as damage dealt|
| | -Display remaining health|
| | -Display outdoor menu if enemy is defeated|
| |2.  Run:|
| | -Displays outdoor menu|
| |Update town menu into outdoor menu|
| |1.  Display the following choices:|
| | -View character|
| | -View map|
| | -Move|
| | -Exit game|
| |2.  If player ran, view character and view map brings player back into combat|
| |3.  If brought into combat, enemy will recover all its health|
| |Test combat menu|
| |1.  Attack:|
| | -Damage is between 2-4|
| | -Damage dealt is displayed correctly|
| | -Player remaining health is displayed correctly|
| | -Enemy remaining health is displayed correctly|
| | -Outdoor menu is displayed after enemy is defeated|
| |2.  Run:|
| | -Outdoor menu is displayed|
| |Test outdoor menu|
| |1.  The correct choices are shown|
| |2.  If player ran, player is brought back into combat menu if view character or view map is chosen|
| |3.  If brought back into combat, enemy has recovered all its health|
|4|Saving player progress|
| |1.  New game:|
| | -New game is created with the player starting at the original position with full health.|
| |2.  Save game:|
| | -Player progression is saved into .csv file|
| | -Overrides previous save file|
| |3.  Resume game:|
| | -Game reads progress from existing .csv file|
| |4.  Exit game:|
| | -Program stops running|
| |Testing player saves|
| |1.  New game:|
| | -Player should be at full health|
| | -Player should have no progress|
| |2.  Save game:|
| | -Player progress is written into a .csv file|
| | -.csv file is created if there is no existing one|
| | -Existing .csv file is overwritten|
| |3.  Resume game:|
| | -Program successfully reads save file|
| | -Displays error message if unable to do so|
| |4.  Exit game:|
| | -Program stops running successfully|
