from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QEvent
import sys
from Mobile import Mobile
from Ship import Ship
from World import World
from random import randint
from Bullet import Bullet


class Controller(object):
    def __init__(self):
        self.ship = Ship(None, 46, 40, 460, 770)
        self.obstacles = []
        self.world = World(self)
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
        pixels = self.controller.check_borders()
        directions = []
        for key in self.keys:
            if key.value == True:
                directions.append(key)
        for direction in directions:
            while self.keys[direction] == True:
                loc = self.ship.move(direction, pixels)
                #self.world.update_ship_position()

    def create_obstacle(self):
        sizes = [[100, 200], [200, 100], [50, 250], [250, 50], [100, 100], [50, 50], [50, 100], [100, 50]]
        size = sizes[randint(0, len(sizes)-1)]
        obstacle = Mobile(None, size[0], size[1], 0, 0)
        self.world.update_obstacle_positions(obstacle)
        return obstacle

    def create_ship(self):
        image = "test.png"
        ship = Ship(image, 10, 10, 500, 100)
        self.ship = ship

    def move_obstacles(self):
        for obs in self.obstacles:
            obs.move(10)
            self.world.update_obstacle_positions(obs)
            if obs.y > self.screenWidth:
                self.obstacles.remove(obs)

    def remove_obstacle(self, obstacle):
        self.obstacles.remove(obstacle)

    def can_shoot(self, seconds):
        if seconds >= 2:
            return True
        else:
            return False

    def shoot(self, screenYWidth=900):
        self.ship.bullet = Bullet(10, 10, self.ship.x, self.ship.y)
        while self.ship.bullet.y >= screenYWidth:
            self.ship.bullet.move(3)
            self.world.update_bullet_position()

    def remove_bullet(self):
        self.ship.bullet = None

