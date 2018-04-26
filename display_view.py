import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia

class MainWidget(QtWidgets.QWidget):
    def __init__(self, controller, parent=None):
        super(MainWidget, self).__init__(parent)
        self.controller = controller
        self.timer = QtCore.QBasicTimer()
        self.timer.stop()
