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
        self.obstacles = []
        self.world = World(self)
        self.keys = []
        self.world = World(self)
        self.keys = {
            "right" : False,
            "left" : False,
            "up" : False,
            "down" : False}
        self.screenWidth = None

    def move_ship(self):
        #
        #   simplified into 1 method as opposed to 4
        #
        pixels = 10
        directions = []
        for key in self.keys:
            if key.value == True:
                directions.append(key)
        for direction in directions:
            while self.keys[direction] == True:
                loc = self.ship.move(direction, pixels)
                self.world.update_ship_position(loc, self.ship.height, self.ship.width)
                self.ship.move(direction, pixels)

    def create_obstacle(self):
        sizes = [[100, 200], [200, 100], [50, 250], [250, 50], [100, 100], [50, 50], [50, 100], [100, 50]]
        size = sizes[randint(0, 7)]
        obstacle = Mobile(None, size[0], size[1], 0, 0)
        self.world.update_obstacle_positions()
        return obstacle

    def create_ship(self):
        image = "test.png"
        ship = Ship(image, 10, 10, 500, 100)
        self.ship = ship

    def move_obstacles(self):
        pixels = 10
        for obs in self.obstacles:
            obs.move(pixels)
            if obs.y > self.screenWidth:
                self.obstacles.remove(obs)
        self.world.update_obstacle_positions()


    def lose_life(self):
        bool = self.world.detect_collision()
        if bool:
            self.ship.lose_life()
        else:
            pass

