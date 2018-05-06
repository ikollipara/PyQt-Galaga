import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia
from Controller import Controller
from random import randint


class MainWidget(QtWidgets.QWidget):
    def __init__(self, controller, parent=None):
        super(MainWidget, self).__init__(parent)
        self.obstacles = []
        self.controller = controller
        self.layout = QtWidgets.QGraphicsGridLayout()
        #self.background = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32)
        self.background = QtGui.QPixmap('.\Images\Tie-dye.jpg')
        #self.background.fill(1)
        self.ship = QtGui.QPixmap('.\Images\ShipIcon.PNG')
        self.setup_obs_creation_timer()
        self.screen_timer()

    def setup_obs_creation_timer(self):
        self.Timer = QtCore.QTimer()
        self.Timer.timeout.connect(self.paint_obstacles)
        self.Timer.start(1000)

    def screen_timer(self):
        self.moveTimer = QtCore.QTimer()
        self.moveTimer.timeout.connect(self.move_obstacles)
        self.moveTimer.start(50)

    def paint_obstacles(self):
        obs = self.controller.create_obstacle()
        obs.x = randint(0, self.width())
        obs.image = QtGui.QImage(obs.width, obs.height, QtGui.QImage.Format_RGB32)
        colors = ['#b0c56f', '#ffd700', '#cc0000', '#a43931', '#006666', '#ff66cd', '#bdc3c7', '#350715', '#6f85c5',
                  '#7eb546', '#19a35e', '#663399']
        color = colors[randint(0, len(colors)-1)]
        obs.image.fill(QtGui.QColor(color))
        self.obstacles.append(obs)

    def move_obstacles(self):
        pixels = 10
        for obs in self.obstacles:
            obs.move(pixels)
            if obs.y > self.width():
                self.obstacles.remove(obs)
        self.update()

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)
        size = self.size()
        pixSize = self.ship.size()
        self.background = self.background.scaled(size)
        #painter.drawImage(0, 0, self.background)
        painter.drawPixmap(0, 0, self.background)
        painter.drawPixmap(self.controller.ship.loc[0], self.controller.ship.loc[1], self.ship)
        if len(self.obstacles) > 0:
            for obstacle in self.obstacles:
                painter.drawImage(obstacle.x, obstacle.y, obstacle.image)





