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
        self.create_actions()
        self.create_menus()
        self.create_lifeBar()

    def setup_window(self):
        xSize = 1000
        ySize = 900
        self.resize(xSize, ySize)
        desktop = QtWidgets.QDesktopWidget().screenGeometry()
        gameWindow = self.geometry()
        xloc = (desktop.width() - gameWindow.width())/2
        yLoc = (desktop.height() - gameWindow.height())/2
        self.move(xloc, yLoc)
        self.setWindowTitle('Atario')
        self.setWindowIcon(QtGui.QIcon('.\Images\Window Icon.jpg'))

    def create_actions(self):
        self.aboutAction = QtWidgets.QAction("&About", self, statusTip="More information about the program", triggered=self.about)
        self.scoresAction = QtWidgets.QAction('H&igh Scores', self, statusTip='Current High Scores', triggered=self.high_scores)

    def create_menus(self):
        self.menu = self.menuBar()
        self.menu.addAction(self.scoresAction)
        self.menu.addAction(self.aboutAction)

    def create_lifeBar(self):
        self.statusBar().showMessage("Lives:{}".format(self.controller.ship.lives))


    def quit(self):
        self.close()

    def about(self):
        QtWidgets.QMessageBox.about(self, 'Atario',
                                         """This program was developed by
Ian, Tessa, and Collin over the course of 4 weeks""")

    def high_scores(self):
        QtWidgets.QMessageBox.about(self, 'Atario High Scores', """Test""")

    def keyPressEvent(self, event):
        if event.key() in [QtCore.Qt.Key_D, QtCore.Qt.Key_Right]:
            pixels = 15
            if self.controller.ship.x > self.width():
                pixels = self.width() - self.controller.ship.x
            self.controller.move_ship_right(pixels)
            self.update()
        elif event.key() in [QtCore.Qt.Key_A, QtCore.Qt.Key_Left]:
            pixels = 15
            if not self.controller.ship.x < 0:
                self.controller.move_ship_left(pixels)
            self.update()
        elif event.key() in [QtCore.Qt.Key_W, QtCore.Qt.Key_Up]:
            pixels = 15
            if not self.controller.ship.y < 0:
                self.controller.move_ship_forward(pixels)
            self.update()
        elif event.key() in [QtCore.Qt.Key_S, QtCore.Qt.Key_Down]:
            pixels = 15
            if self.controller.ship.y > self.height():
                pixels = self.height() - self.controller.ship.y
            self.controller.move_ship_back(pixels)
            self.update()
