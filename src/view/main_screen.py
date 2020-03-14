# src/view/main_screen.py
# Ian Kollipara
# 2020.03.12
# Main Screen for Atario
#
# Usage
# from view.main_screen import Main_Screen

# Imports
from PyQt5 import QtGui, QtWidgets, QtCore

class Main_Screen(QtWidgets.QWidget):
    """ Main Screen for Atario. """

    # Instance Variables(private)
    # controller  Main Controller instance passed in

    def __init__(self, controller):
        """ __init__() create Main_Screen object. 
        
        Parameters
        controller  Controller Instance from Main_Window passed in
        """

        super(Main_Screen, self).__init__()
        self.controller = controller

        self._start_game_timer()
        self._start_obsctacle_creation_timer()
        self._start_clock()
    
    def _start_game_timer(self):
        """ Start main game timer. 
        
        Timer runs at 60ms and timeouts
        for location updates and collision
        updates, as well as screen updates.
        """

        self.game_timer = QtCore.QTimer()
        self.game_timer.timeout.connect(self.controller.update_obstacle_locations)
        self.game_timer.timeout.connect(self.controller.detect_collision)
        self.game_timer.timeout.connect(self.update)
        self.game_timer.start(60)
    
    def _start_obsctacle_creation_timer(self):
        """ Start Obstacle Creation Timer. 
        
        Timer runs at 475ms and timeouts
        for obstacle creation.
        """

        self.creation_timer = QtCore.QTimer()
        self.creation_timer.timeout.connect(self.controller.create_obstacles)
        self.creation_timer.start(475)
    
    def _start_clock(self):
        """ Start game clock. 
        
        Timer runs at 1s and timeouts
        for add_second
        """

        self.clock = QtCore.QTimer()
        self.clock.timeout.connect(self.controller.add_second)
        self.clock.start(1000)

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)
        background = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32).scaled(self.size())
        painter.drawImage(0,0, background)
        ship_location, ship_image = self.controller.get_ship()
        painter.drawPixmap(QtCore.QPoint(ship_location[0], ship_location[1]), ship_image)
        for obstacle in self.controller.get_obstacle_total():
            painter.drawImage(QtCore.QPoint(obstacle.location[0], obstacle.location[1]), obstacle.color)
        