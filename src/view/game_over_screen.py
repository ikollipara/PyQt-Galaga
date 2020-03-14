# src/view/game_over_screen.py
# Ian Kollipara
# 2020.03.12
# Game Over Screen used in Atario
# 
# Usage
# from view.game_over_screen import Game_Over_Screen

# Imports
from PyQt5 import QtGui, QtWidgets, QtCore

class Game_Over_Screen(QtWidgets.QWidget):
    """ Game Over Screen used at the end of Atario. """

    # Instance Variables (private)
    # controller  Main Controller instance passed in

    def __init__(self, controller):
        """ __init__() create Game_Over_Screen object. 
        
        Parameters
        controller  Controller Instance from Main_Window passed in
        """

        super(Game_Over_Screen, self).__init__()
        self.controller = controller
        
        # Screen Initialization
        self._init_subwidgets()
        self._setup_layout()
    
    def _init_subwidgets(self):
        """ Create widgets used in Game_Over_Screen. """
        
        self.game_over_logo = QtWidgets.QLabel()
        self.game_over_logo.setPixmap(QtGui.QPixmap("src/images/Game Over.PNG"))
        self.game_over_logo.setAlignment(QtCore.Qt.AlignHCenter)
    
    def _setup_layout(self):
        """ Set layout for Game_Over_Screen. """

        total_layout = QtWidgets.QVBoxLayout()
        total_layout.addStretch()
        total_layout.addWidget(self.game_over_logo)
        total_layout.addStretch()

        self.setLayout(total_layout)