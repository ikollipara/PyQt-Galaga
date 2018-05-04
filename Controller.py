from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QEvent
import sys
from Mobile import Mobile
from Ship import Ship
from random import randint

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
        #obsDict = {'long': [10, 20],
        #           'fat': [20, 10]}
        #obsList = obsDict.keys()
        #image = obsList[randint(0, 1)]
        obstacle = Mobile(None, 100, 100, 0, 0)
        return obstacle

    def create_ship(self):
        image = "test.png"
        ship = Ship(image, 10, 10, 500, 100)
        self.ship = ship
