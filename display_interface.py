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
        self.setup_statusBar()
        self.statusTimer()


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

    def statusTimer(self):
        self.statTimer = QtCore.QTimer()
        self.statTimer.timeout.connect(self.setup_statusBar)
        self.statTimer.start(10)

    def setup_statusBar(self):
        time = self.setup_UserTime()
        self.controller.ship.time = time
        self.statusBar().showMessage('Lives:{} | Time: {}'.format(self.controller.ship.lives, time))

    def setup_UserTime(self):
        time = self.display.userTime
        if time/60 == 1:
            self.display.minutes += 1
            self.display.userTime = 0
        if self.display.minutes != 0:
            showTime = str(self.display.minutes)
            if len(str(self.display.userTime)) == 1:
                showTime = showTime + ':0' + str(self.display.userTime)
            else:
                showTime = showTime + ":" + str(self.display.userTime)
        else:
            showTime = str(self.display.userTime)
        return showTime

    def quit(self):
        self.close()

    def about(self):
        QtWidgets.QMessageBox.about(self, 'Atario',
                                         """This program was developed by
Ian, Tessa, and Collin over the course of 4 weeks""")

    def high_scores(self):
        QtWidgets.QMessageBox.about(self, 'Atario High Scores', """Test""")

    def check_borders(self):
        self.pixels = 20
        keys = self.controller.keys
        if keys["right"] == True and self.controller.ship.x + 20 > (self.width() - 40):
            self.pixels = 0
        if keys["left"] == True and self.controller.ship.x - 20 < 0:
            self.pixels = 0
        if keys["up"] == True and self.controller.ship.y < 0:
            self.pixels = 0
        if keys["down"] == True and self.controller.ship.y > (self.height() - 100):
            self.pixels = 0
        return self.pixels

    def keyPressEvent(self, event):
        #
        #   connect method to timer in order for movement to work
        #       updates values correctly. timer must see if controller.keys[value] == True
        #       while value == True: move_ship (simplified method in
        #
        key = event.key()
        if key in [QtCore.Qt.Key_D, QtCore.Qt.Key_Right]:
            self.controller.keys["right"] = True
            direction = "right"
            pixels = self.check_borders()
            loc = self.controller.ship.move(direction, pixels)
            self.controller.world.update_ship_position()
        elif key in [QtCore.Qt.Key_A, QtCore.Qt.Key_Left]:
            self.controller.keys["left"] = True
            direction = "left"
            pixels = self.check_borders()
            loc = self.controller.ship.move(direction, pixels)
            self.controller.world.update_ship_position()
        elif key in [QtCore.Qt.Key_W, QtCore.Qt.Key_Up]:
            self.controller.keys["up"] = True
            direction = "up"
            pixels = self.check_borders()
            loc = self.controller.ship.move(direction, pixels)
            self.controller.world.update_ship_position()
        elif key in [QtCore.Qt.Key_S, QtCore.Qt.Key_Down]:
            self.controller.keys["down"] = True
            direction = "down"
            pixels = self.check_borders()
            loc = self.controller.ship.move(direction, pixels)
            self.controller.world.update_ship_position()
        elif key in [QtCore.Qt.Key_Space]:
            self.display.paint_bullet()
            canShoot = self.controller.can_shoot(self.display.userTime)
            if canShoot:
                self.controller.shoot()
        pixels = self.check_borders()

    #def processKeyEvent(self, event):
    #    isPress = event.modifiers()
    #    key = event.key()
    #    directions  = {
    #        "right":[QtCore.Qt.Key_D, QtCore.Qt.Key_Right],
    #        "left":[QtCore.Qt.Key_A, QtCore.Qt.Key_Left],
    #        "up":[QtCore.Qt.Key_W, QtCore.Qt.Key_Up],
    #        "down":[QtCore.Qt.Key_S, QtCore.Qt.Key_Down]
    #    }
    #    if key in directions["right"]:
    #        direction = "right"
    #    elif key in directions["left"]:
    #        direction = "left"
    #    elif key in directions["up"]:
    #        direction = "up"
    #    elif key in directions["down"]:
    #        direction = "down"
    #    pixels = 10
    #    if isPress == True:
    #        loc = self.controller.ship.move(direction, pixels)
    #        self.controller.world.update_ship_position(loc, self.controller.ship.height, self.controller.ship.width)
    #        self.controller.ship.move(direction, pixels)
    #        self.update()
    #    else:
    #        pass

    def keyReleaseEvent(self, event):
        key = event.key()
        if not event.isAutoRepeat():
            if key in [QtCore.Qt.Key_D, QtCore.Qt.Key_Right]:
                self.controller.keys["right"] = False
            elif key in [QtCore.Qt.Key_A, QtCore.Qt.Key_Left]:
                self.controller.keys["left"] = False
            elif key in [QtCore.Qt.Key_W, QtCore.Qt.Key_Up]:
                self.controller.keys["up"] = False
            elif key in [QtCore.Qt.Key_S, QtCore.Qt.Key_Down]:
                self.controller.keys["down"] = False
            elif key in [QtCore.Qt.Key_Space]:
                pass

        self.pixels = 20
