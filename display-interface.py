from PyQt5 import QtGui, QtCore, QtWidgets
from Controller import Controller
from display_view import MainWidget
import sys

class GameWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        super(GameWindow, self).__init__()
        self.app = app
        self.controller = Controller()
        self.setup_window()
        self.display = MainWidget(self.controller)
        self.setCentralWidget(self.display)
        self.display.show()

    def setup_window(self):
        xSize = 1000
        ySize = 1500
        self.resize(xSize, ySize)
        desktop = QtWidgets.QDesktopWidget().screenGeometry()
        gameWindow = self.geometry()

# region Test Main
pyQtApp = QtWidgets.QApplication(sys.argv)
x = GameWindow(pyQtApp)
x.show()
exitCondition = pyQtApp.exec_()
sys.exit(exitCondition)
# endregion