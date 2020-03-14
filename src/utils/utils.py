# src/utils/utils.py
# Ian Kollipara
# 2020.03.12
# Collision Utils
#
# Usage
# from utils import ...

# Imports
from typing import Tuple, List, Union
from model.ship import Ship
from model.obstacle import Obstacle


def check_collision(ship: Ship, obstacles: List[Obstacle]) -> Tuple[bool, Obstacle]:
    """ Check if ship has collided with any obstacles. Return a Tuple.

    Parameters
    ship       Current Ship instance
    obstacles  Current active obstacles
    """

    ship_collision_box = create_collision_box(ship)

    for obstacle in obstacles:
        collision = 0
        obstacle_collision_box = create_collision_box(obstacle)

        for pixel in obstacle_collision_box[0]:

            if pixel in ship_collision_box[0]:

                if collision == 0:
                    collision += 1

        for pixel in obstacle_collision_box[1]:

            if pixel in ship_collision_box[1]:
                
                if collision == 1:
                    collision += 1

        if collision == 2:
            return True, obstacle

    return False, None


def create_collision_box(obj: Union[Ship, Obstacle]) -> Tuple[List[int], List[int]]:
    """ Create new collision box for object. Return a Tuple 

    Parameters
    obj  Either ship or Obstacle instance
    """

    top_left = obj.location
    bottom_right = (obj.size[0] + obj.location[0],
                    obj.size[1] + obj.location[1])

    left_pixels = [i for i in range(top_left[0], bottom_right[0] + 1)]
    bottom_pixels = [i for i in range(top_left[1], bottom_right[1] + 1)]

    return (left_pixels, bottom_pixels)
