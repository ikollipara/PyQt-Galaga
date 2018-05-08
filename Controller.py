from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QEvent
import sys
from Mobile import Mobile
from Ship import Ship
from World import World
from random import randint

class Controller(object):
    def __init__(self):
        self.ship = Ship(None, 4, 4, 460, 770)
        self.world = World()
        self.keys = {
            "right" : False,
            "left" : False,
            "up" : False,
            "down" : False}

    def move_ship_right(self, pixels):
        loc = self.ship.move("right", pixels)
        self.world.update_positions(loc, self.ship.height, self.ship.width)
        self.ship.move("right", pixels)

    def move_ship_left(self, pixels):
        loc = self.ship.move("left", pixels)
        self.world.update_positions(loc, self.ship.height, self.ship.width)
        self.ship.move("left", pixels)

    def move_ship_forward(self, pixels):
        loc = self.ship.move("forward", pixels)
        self.world.update_positions(loc, self.ship.height, self.ship.width)
        self.ship.move("forward", pixels)

    def move_ship_back(self, pixels):
        loc = self.ship.move("back", pixels)
        self.world.update_positions(loc, self.ship.height, self.ship.width)
        self.ship.move("back", pixels)

    def create_obstacle(self):
        sizes = [[100, 200], [200, 100], [50, 250], [250, 50], [100, 100], [50, 50], [50, 100], [100, 50]]
        size = sizes[randint(0, 7)]
        obstacle = Mobile(None, size[0], size[1], 0, 0)
        return obstacle

    def create_ship(self):
        image = "test.png"
        ship = Ship(image, 10, 10, 500, 100)
        self.ship = ship

    def move_obstacles(self):
        for obstacle in self.obstacles:
            location = obstacle.move("forward", 3)
            self.world.update_positions(location, self.ship.height, self.ship.width)
