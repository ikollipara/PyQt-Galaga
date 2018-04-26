import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia
from Controller import Controller

class MainWidget(QtWidgets.QWidget):
    def __init__(self, controller, parent=None):
        super(MainWidget, self).__init__(parent)
        self.controller = controller
        self.timer = QtCore.QBasicTimer()
        self.timer.stop()

    def keyPressEvent(self, event):
        # keyCode = QtGui.QKeyEvent.key
        # if keyCode == 57:
        #     print('57')
        # elif keyCode == "0x57":
        #     print("0x57")
        if event.key() in [QtCore.Qt.Key_D]:
            Controller.move_right()
        elif event.key() in [QtCore.Qt.Key_D]:
            Controller.move_left()

