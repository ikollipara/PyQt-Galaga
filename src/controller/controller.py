# src/controller/controller.py
# Ian Kollipara
# 2020.03.12
# Main Controller in Atario
#
# Usage
# from controller.controller import Controller

# Imports
from model.game_model import Model
from model.obstacle import Obstacle
from utils.type_defs import Screen, View
from utils.utils import check_collision
from PyQt5.QtGui import QImage, QColor, QPixmap
from random import randint, choice
from typing import Tuple

# Constants
OBSTACLE_SIZES = [(100, 200), (200, 100), (50, 250), (250, 50),
                  (100, 100), (50, 50), (50, 100), (100, 50)]
OBSTACLE_COLORS = ['#b0c56f', '#ffd700', '#cc0000', '#a43931', '#006666',
                   '#ff66cd', '#bdc3c7', '#350715', '#6f85c5', '#7eb546', '#19a35e', '#663399']


class Controller:
    """ Main Controller used in Atario. 

    The Controller in the MVC. Handles
    all processing of data between the 
    view and model.
    """

    # Instance Variables (private)
    # model  Only instance of Model class

    def __init__(self) -> None:
        """ __init__() create Controller object. 

        Handles any data processing and transfer
        between the view (main_window) and model (game_model).
        """

        self.model = Model()

    def get_current_screen(self) -> View:
        """ Retrieve current screen class. """

        return self.model.screens[self.model.current_screen]

    def set_current_screen(self, screen: Screen) -> None:
        """ Set current screen key. """

        if screen in self.model.screens.keys():
            self.model.current_screen = screen

        else:
            raise KeyError(f"{screen} is not a key in Model.screens")

    def get_time(self) -> str:
        """ Retrieve and Format Model's time. """

        minutes = 0
        seconds = self.model.time

        while seconds >= 60:
            minutes += 1
            seconds -= 60

        return f"{minutes}:{seconds:0>2d}" if minutes > 0 else f"{seconds:0>2d}"

    def update_screen_size(self, width: int, height: int) -> None:
        self.model.screen_size = (width, height)

    def create_obstacles(self) -> None:
        """ Create and append obstacle to model"""

        obstacle_size = choice(OBSTACLE_SIZES)
        obstacle_color = choice(OBSTACLE_COLORS)

        obstacle = Obstacle((0, 0), obstacle_size, QImage(
            obstacle_size[0], obstacle_size[1], QImage.Format_ARGB32))
        obstacle.color.fill(QColor(obstacle_color))
        obstacle.location = (
            randint(0, self.model.screen_size[0] - obstacle.size[0]), -obstacle.size[1])

        self.model.current_obstacles.append(obstacle)

    def update_obstacle_locations(self) -> None:
        """ Update Obstacle location. """

        for obstacle in self.model.current_obstacles:
            obstacle.location = (
                obstacle.location[0], obstacle.location[1] + self.model.obstacle_movement_speed)

    def update_ship_location(self, direction):
        """ Update Ship location. 

        Parameters
        direction  String used in if-else case statement
        """

        pixels = 20

        if direction == "right" and not self.model.ship.location[0] + pixels > self.model.screen_size[0] - self.model.ship.size[0]:
            self.model.ship.location = (
                self.model.ship.location[0] + pixels, self.model.ship.location[1])

        elif direction == "left" and not self.model.ship.location[0] - pixels < 0:
            self.model.ship.location = (
                self.model.ship.location[0] - pixels, self.model.ship.location[1])

        elif direction == "up" and not self.model.ship.location[1] < 0:
            self.model.ship.location = (
                self.model.ship.location[0], self.model.ship.location[1] - pixels)

        elif direction == "down" and not self.model.ship.location[1] > self.model.screen_size[1] - self.model.ship.size[1]:
            self.model.ship.location = (
                self.model.ship.location[0], self.model.ship.location[1] + pixels)

    def detect_collision(self):
        """ Detect collision and update model. """

        has_collided, obstacle = check_collision(
            self.model.ship, self.model.current_obstacles)

        if has_collided:
            self.model.ship.lives -= 1
            self.model.current_obstacles.remove(obstacle)

        if not self.model.ship.lives:
            self.model.current_screen = "Game Over"

    def add_second(self):
        """ Add one second to model.time. """

        self.model.time += 1

    def go_to_main(self):
        """ Set current_screen to Main. """

        self.model.current_screen = "Main"

    def get_ship(self) -> Tuple[Tuple[int, int], QPixmap]:
        """ Return Ship Data. """

        return self.model.ship.location, self.model.ship.image

    def get_ship_lives(self) -> int:
        """ Retieve current ship instance life count. """

        return self.model.ship.lives

    def get_obstacle_total(self):
        """ Return Obstacle List. """

        return self.model.current_obstacles
