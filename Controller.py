from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QEvent
import sys
from Mobile import Mobile
from Ship import Ship
from World import World

class Controller(object):
    def __init__(self):
        self.obstacles = []
        self.ship = None
        self.world = World()

    def move_ship_right(self):
        location = self.ship.move("right", 3)
        self.world.update_positions(location, self.ship.height, self.ship.width)

    def move_ship_left(self):
        location = self.ship.move("left", 3)
        self.world.update_positions(location, self.ship.height, self.ship.width)

    def create_obstacle(self):
        image = "test.png"
        obstacle = Mobile(image, 10, 10, 900, 800)
        self.obstacles.append(obstacle)

    def create_ship(self):
        image = "test.png"
        ship = Ship(image, 10, 10, 500, 100)
        self.ship = ship

    def move_obstacles(self):
        for obstacle in self.obstacles:
            location = obstacle.move("forward", 3)
            self.world.update_positions(location, self.ship.height, self.ship.width)
