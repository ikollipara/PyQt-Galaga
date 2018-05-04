
import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia
from Controller import Controller


class MainWidget(QtWidgets.QWidget):
    def __init__(self, controller, parent=None):
        super(MainWidget, self).__init__(parent)
        self.obstacles = []
        self.controller = controller
        self.layout = QtWidgets.QGraphicsGridLayout()
        self.background = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32)
        self.background.fill(1)
        self.ship = QtGui.QPixmap('.\Images\ShipIcon.PNG')
        self.test()
        self.setup_obs_creation_timer()
        self.screen_timer()

    def setup_obs_creation_timer(self):
        self.Timer = QtCore.QTimer()
        self.Timer.timeout.connect(self.show_obstacles)
        self.Timer.start(5000)

    def screen_timer(self):
        self.moveTimer = QtCore.QTimer()
        self.moveTimer.timeout.connect(self.move_obstacles)
        self.moveTimer.start(10)

    def show_obstacles(self):
        obs = self.controller.create_obstacle()
        obsImage = QtGui.QImage(obs.width, obs.height, QtGui.QImage.Format_RGB32)
        obsImage.fill(0)
        obs.image = obsImage
        self.obstacles.append(obs)

    def test(self):
        self.obs = self.controller.create_obstacle()
        self.obsImage = QtGui.QImage(self.obs.width, self.obs.height, QtGui.QImage.Format_RGB32)
        self.obsImage.fill(QtGui.QColor('#ffffff'))


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
        painter.drawImage(0, 0, self.background)
        painter.drawPixmap(self.controller.ship.loc[0], self.controller.ship.loc[1], self.ship)
        painter.drawImage(self.obs.x, self.obs.y, self.obsImage)




