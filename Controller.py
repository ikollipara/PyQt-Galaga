from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QEvent
import sys
from Mobile import Mobile
from Ship import Ship

class Controller(object):
    def __init__(self):
        self.obstacles = []
        self.ship = Ship(None, 3, 3, 0, 0)

    def move_ship_right(self):
        self.ship.move("right", 15)

    def move_ship_left(self):
        self.ship.move("left", 15)

    def create_obstacle(self):
        image = "test.png"
        obstacle = Mobile(image, 10, 10, 900, 800)
        self.obstacles.append(obstacle)

    def create_ship(self):
        image = "test.png"
        ship = Ship(image, 10, 10, 500, 100)
        self.ship = ship
