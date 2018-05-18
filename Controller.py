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
        self.obstSpeed = 10
        self.obstacles = []
        self.world = World(self)
        self.world = World(self)
        self.keys = {
            "right" : False,
            "left" : False,
            "up" : False,
            "down" : False}
        self.screenWidth = None
        self.screenHeight = None

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
            obs.move(self.obstSpeed)
            self.world.update_obstacle_positions(obs)
            if obs.y > self.screenHeight:
                self.obstacles.remove(obs)

    def remove_obstacle(self, obstacle):
        self.obstacles.remove(obstacle)

    def create_bullet(self):
        x = int(self.ship.loc[0] + self.ship.width/2)
        y = 1 + self.ship.loc[1]
        bullet = Bullet(None, 10, 10, x, y)
        self.world.update_bullet_position(bullet)
        return bullet

    def move_bullets(self):
        for bullet in self.ship.bullets:
            bullet.move(30)
            self.world.update_bullet_position(bullet)
            if bullet.loc[1] < 0:
                self.ship.bullets.remove(bullet)


