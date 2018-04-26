import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia

class MainWidget(QtWidgets.QWidget):
    def __init__(self, controller, parent=None):
        super(MainWidget, self).__init__(parent)
        self.controller = controller
        self.background = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32)
        self.background.fill(1)

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)
        size = self.size()
        self.background = self.background.scaled(size)
        painter.drawImage(0, 0, self.background)

