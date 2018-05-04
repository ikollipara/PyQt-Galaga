from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QEvent
import sys
from Mobile import Mobile
from Ship import Ship

class Controller(object):
    def __init__(self):
        self.obstacles = []
        self.ship = Ship(None, 3, 3, 100, 150)

    def move_ship_right(self, pixels):
        self.ship.move("right", pixels)

    def move_ship_left(self, pixels):
        self.ship.move("left", pixels)

    def move_ship_forward(self, pixels):
        self.ship.move("forward", pixels)

    def move_ship_back(self, pixels):
        self.ship.move("back", pixels)

    def create_obstacle(self):
        image = "Untitled.png"
        obstacle = Mobile(image, 10, 10, 900, 800)
        self.obstacles.append(obstacle)

    def create_ship(self):
        image = "test.png"
        ship = Ship(image, 10, 10, 500, 100)
        self.ship = ship
