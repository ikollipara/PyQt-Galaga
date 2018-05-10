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
        self.world = World()
        self.keys = []
        self.screenWidth = None

    def move_ship_right(self, pixels):
        loc = self.ship.move("right", pixels)
        self.world.update_ship_position(loc, self.ship.height, self.ship.width)
        self.keys.append("right")
        self.ship.move("right", pixels)

    def move_ship_left(self, pixels):
        loc = self.ship.move("left", pixels)
        self.world.update_ship_position(loc, self.ship.height, self.ship.width)
        self.keys.append("left")
        self.ship.move("left", pixels)

    def move_ship_forward(self, pixels):
        loc = self.ship.move("forward", pixels)
        self.world.update_ship_position(loc, self.ship.height, self.ship.width)
        self.keys.append("up")
        self.ship.move("forward", pixels)

    def move_ship_back(self, pixels):
        loc = self.ship.move("back", pixels)
        self.world.update_ship_position(loc, self.ship.height, self.ship.width)
        self.keys.append("down")
        self.ship.move("back", pixels)

    def create_obstacle(self):
        sizes = [[100, 200], [200, 100], [50, 250], [250, 50], [100, 100], [50, 50], [50, 100], [100, 50]]
        size = sizes[randint(0, 7)]
        obstacle = Mobile(None, size[0], size[1], 0, 0)
        return obstacle


    def move_obstacles(self):
        pixels = 10
        for obs in self.obstacles:
            obs.move(pixels)
            self.world.update_obstacle_position(obs.loc, obs.height, obs.width)
            if obs.y > self.screenWidth:
                self.obstacles.remove(obs)

    def lose_life(self):
        bool = self.world.detect_collision()
        if bool:
            self.ship.lose_life()
        else:
            pass
