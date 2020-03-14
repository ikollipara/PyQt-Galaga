# src/model/ship.py
# Ian Kollipara
# 2020.03.12
# Ship Model for Player
# 
# Usage
# from ship import Ship

# Imports
from PyQt5.QtGui import QPixmap
from typing import Tuple

# Constants
DEFAULT_LIVES_COUNT = 3

class Ship:
    """ Ship Model used for Player Ship. 
    
    Contains ship location, ship size, 
    ship image, and ship lives.
    """

    # Instance Variables (private)
    # image     Imagefile used to display Ship on screen
    # location  Top-Left Point of ship. Ex. (0,0)
    # size      Tuple of Height and Width Ex. (100, 40)
    # lives     Integer representing total lives left

    def __init__(self) -> None:
        self.location: Tuple[int, int] = (460,770)
        self.size: Tuple[int, int] = (40,46)
        self.lives: int = DEFAULT_LIVES_COUNT
        self.image = QPixmap("src/images/ShipIcon.PNG")
    