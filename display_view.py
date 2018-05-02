import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia
from Controller import Controller


class MainWidget(QtWidgets.QWidget):
    def __init__(self, controller, parent=None):
        super(MainWidget, self).__init__(parent)
        self.controller = controller
        self.layout = QtWidgets.QGraphicsGridLayout()
        self.background = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32)
        self.background.fill(1)
        self.ship = QtGui.QPixmap('.\Images\ShipIcon.PNG')
        self.timer_setup()


    def timer_setup(self):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(100)

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)
        size = self.size()
        pixSize = self.ship.size()
        self.background = self.background.scaled(size)
        painter.drawImage(0, 0, self.background)
        painter.drawPixmap(0, 0, self.ship)

    def keyPressEvent(self, event):
        if event.key() in [QtCore.Qt.Key_D]:
            Controller.move_ship_right()
        elif event.key() in [QtCore.Qt.Key_A]:
            Controller.move_ship_left()

