# src/utils/type_defs.py
# Ian Kollipara
# 2020.03.12
# type definitions for use in Atario
#
# Usage
# from type_defs import ...

# Imports
from typing import *
from view.game_over_screen import Game_Over_Screen
from view.main_screen import Main_Screen
from view.start_screen import Start_Screen

Matrix = List[List[int]]
Screen = str
View = Union[Start_Screen, Main_Screen, Game_Over_Screen]
