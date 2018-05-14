import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia
from Controller import Controller
from random import randint


class MainWidget(QtWidgets.QWidget):
    def __init__(self, controller, parent=None):
        super(MainWidget, self).__init__(parent)
        self.userTime = 0
        self.minutes = 0
        self.controller = controller
        self.background = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32)
        #self.background = QtGui.QPixmap('.\Images\Tie-dye.jpg')
        self.background.fill(1)
        self.ship = QtGui.QPixmap('.\Images\ShipIcon.PNG')
        self.shipBox = QtGui.QImage(self.controller.ship.width, self.controller.ship.height, QtGui.QImage.Format_RGB32)
        self.shipBox.fill(QtGui.QColor('#006666'))
        self.setup_obs_creation_timer()
        self.screen_timer()
        self.user_timer()
        self.game_timer()

    def setup_obs_creation_timer(self):
        self.Timer = QtCore.QTimer()
        self.Timer.timeout.connect(self.paint_obstacles)
        self.Timer.start(500)

    def screen_timer(self):
        self.moveTimer = QtCore.QTimer()
        self.moveTimer.timeout.connect(self.controller.move_obstacles)
        self.moveTimer.start(60)

    def user_timer(self):
        self.uTimer = QtCore.QTimer()
        self.uTimer.timeout.connect(self.add_second)
        self.uTimer.start(1000)

    def game_timer(self):
        self.gTimer = QtCore.QTimer()
        self.gTimer.timeout.connect(self.controller.world.detect_collision)
        self.gTimer.timeout.connect(self.update)
        self.gTimer.start(10)

    def add_second(self):
        self.userTime += 1

    def paint_obstacles(self):
        obs = self.controller.create_obstacle()
        self.controller.screenWidth = self.width()
        obs.x = randint(0, self.width())
        obs.image = QtGui.QImage(obs.width, obs.height, QtGui.QImage.Format_RGB32)
        colors = ['#b0c56f', '#ffd700', '#cc0000', '#a43931', '#006666', '#ff66cd', '#bdc3c7', '#350715', '#6f85c5',
                  '#7eb546', '#19a35e', '#663399']
        color = colors[randint(0, len(colors)-1)]
        obs.image.fill(QtGui.QColor(color))
        self.controller.obstacles.append(obs)

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)
        size = self.size()
        self.background = self.background.scaled(size)
        painter.drawImage(0, 0, self.background)
        #painter.drawPixmap(0, 0, self.background)
        painter.drawPixmap(self.controller.ship.loc[0], self.controller.ship.loc[1], self.ship)
        painter.drawImage(self.controller.ship.loc[0], self.controller.ship.loc[1], self.shipBox)
        if len(self.controller.obstacles) > 0:
            for obstacle in self.controller.obstacles:
                painter.drawImage(obstacle.x, obstacle.y, obstacle.image)





