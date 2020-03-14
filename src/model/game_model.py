# src/model/game_model.py
# Ian Kollipara
# 2020.03.12
# Main Model used in Atario
# 
# Usage
# from model.game_model import Model

# Imports
from view.start_screen import Start_Screen
from view.game_over_screen import Game_Over_Screen
from view.main_screen import Main_Screen
from model.ship import Ship
from typing import List, Dict, Tuple
from model.obstacle import Obstacle
from utils.type_defs import View

class Model:
    """ Main Model used in Atario. 
    
    Contains both Ship and Obstacle data,
    as well as current screen and current time.
    """

    # Instance Variables (private)
    # screen_size              Tuple of screen Height and Width
    # screens                  Dictionary of Screen classes
    # current_screen           Dictionary key used to retrieve Screen class
    # ship                     Current Ship data
    # Obstacles                List of Obstacle Data
    # time                     Current game time
    # obstacle_movement_speed  Integer used for how fast 
    #                          obstacle approach player

    def __init__(self) -> None:
        """ __init__() create Model object. """
        
        self.screens: Dict[str, View] = {
            "Main":      Main_Screen,
            "Start":     Start_Screen,
            "Game Over": Game_Over_Screen,
        }
        self.current_screen = "Start"
        self.ship = Ship()
        self.current_obstacles:List[Obstacle] = []
        self.time = 0
        self.screen_size: Tuple[int, int] = (0,0)
        self.obstacle_movement_speed = 10