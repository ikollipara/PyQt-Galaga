# src/model/obstacle.py
# Ian Kollipara
# 2020.03.12
# Obstacle Model used for enemies
# 
# Usage
# from model.obstacle import Obstacle

# Imports
from typing import Tuple
from PyQt5.QtGui import QImage

class Obstacle:
    """ Obstacle Model used for enemies. 
    
    Contains location, size, lives, and color.
    """

    # Instance Variables (private)
    # location  Top-Left point Ex. (0,0)
    # size      Tuple of Height and Width Ex. (100,40)
    # lives     Integer representing remaining lives
    # color     QImage instance using RGB32 colors

    def __init__(self, location, size, color, lives = 1) -> None:
        self.location: Tuple[int, int] = location
        self.size: Tuple[int, int] = size
        self.color: QImage = color
        self.lives: int = lives
    
