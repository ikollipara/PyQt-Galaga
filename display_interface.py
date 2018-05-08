from PyQt5 import QtGui, QtCore, QtWidgets
from Controller import Controller
from display_view import MainWidget
from random import *
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
        # self.setup_statusBar()


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
        self.lifeAction = QtWidgets.QAction(QtGui.QIcon('.\Images\Hearts.PNG'), "Life", self)


    def create_menus(self):
        self.menu = self.menuBar()
        self.menu.addAction(self.scoresAction)
        self.menu.addAction(self.aboutAction)


    # def setup_statusBar(self):
    #     self.bar = self.statusBar()
    #     self.bar

    def setup_UserTime(self):
        time = self.display.userTime
        if time % 60 == 0:
            time = time/60
            time = int(time)
            time = str(time) + '00'
            time = int(time)
        if len(str(time)) >= 3:
            showTime = str(time)[:-2] + ':' + str(time)[-2:]
        else:
            showTime = str(time)
        return showTime

    def quit(self):
        self.close()

    def about(self):
        QtWidgets.QMessageBox.about(self, 'Atario',
                                         """This program was developed by
Ian, Tessa, and Collin over the course of 4 weeks""")

    def high_scores(self):
        QtWidgets.QMessageBox.about(self, 'Atario High Scores', """Test""")


    def keyPressEvent(self, event):
        key = event.key()
        if key in [QtCore.Qt.Key_D, QtCore.Qt.Key_Right]:
            self.controller.keys["right"] = True
            direction = "right"
            print("right = True")
        elif key in [QtCore.Qt.Key_A, QtCore.Qt.Key_Left]:
            self.controller.keys["right"] = True
            direction = "left"
            print("left = True")
        elif key in [QtCore.Qt.Key_W, QtCore.Qt.Key_Up]:
            self.controller.keys["right"] = True
            direction = "up"
            print("up = True")
        elif key in [QtCore.Qt.Key_S, QtCore.Qt.Key_Down]:
            self.controller.keys["right"] = True
            direction = "down"
            print("down = True")
        return direction

    def keyReleaseEvent(self, event):
        key = event.key()
        if not event.isAutoRepeat():
            if key in [QtCore.Qt.Key_D, QtCore.Qt.Key_Right]:
                self.controller.keys["right"] = False
                print("right = False")
            elif key in [QtCore.Qt.Key_A, QtCore.Qt.Key_Left]:
                self.controller.keys["right"] = False
                print("left = False")
            elif key in [QtCore.Qt.Key_W, QtCore.Qt.Key_Up]:
                self.controller.keys["right"] = False
                print("up = False")
            elif key in [QtCore.Qt.Key_S, QtCore.Qt.Key_Down]:
                self.controller.keys["right"] = False
                print("down = False")

