import json

from backend.classes.stats import Stats
from backend.classes.move import Move

class Pokemon():

    # Allows the Pokemon to take damage
    def takeDmg(self, dmg:int):
        self.curr_hp = max(0, self.curr_hp - int(dmg))

    # Initialises the Pokemon class from a json file
    ### THIS FUNCTION IS FOR YOU TO COMPLETE ###
    def __init__(self, pkmnInfo: json) -> None:

        ### POKEMON CHECKING ###
        
        # ----Your code here---- #
        
        
        
        

        ### STANDARD FIELDS ### (Populating the blank Pokemon card)

        # ----Your code here---- #




        ### SPECIAL FIELDS ### 
        
        # Stats object will help us handle and process the data
        # (Fill in the blank)
        self.stats = Stats()

        # Initialise a list of moves that your pokemon can make (think about Python lists)
        
        # ----Your code here---- #
        
        # For each move in the JSON file use the info to make a move object and append it to the pokemon
        # HINT: Use a for loop ;)
        
        # ----Your code here---- #
    
