# src/view/start_screen.py
# Ian Kollipara
# 2020.03.12
# Start Screen Widget
#
# Usage
# from start_screen import Start_Screen

# Imports
from PyQt5 import QtGui, QtWidgets


class Start_Screen(QtWidgets.QWidget):
    """ Start Screen Widget for Atario. """

    # Instance Variables(private)
    # controller  Main Controller instance passed in

    def __init__(self, controller) -> None:
        """ __init__() create Start_Screen object. 

        Parameters
        controller  Controller Instance from Main_Window passed in
        """

        super(Start_Screen, self).__init__()
        self.controller = controller

        # Widget Initialization
        self._init_subwidgets()
        self._setup_layout()

        self.update()

    def _init_subwidgets(self) -> None:
        """ Create widgets used in Start_Screen. """

        self.game_logo = QtWidgets.QLabel()
        self.game_logo.setPixmap(QtGui.QPixmap("src/images/Logo.PNG"))
        self.start_btn = QtWidgets.QPushButton()

        self.start_btn.setText("Start")
        self.start_btn.clicked.connect(self.controller.go_to_main)

    def _setup_layout(self) -> None:
        """ Set layout for Start_Screen. """

        hortizontal_layout_logo = QtWidgets.QHBoxLayout()
        hortizontal_layout_logo.addStretch()
        hortizontal_layout_logo.addWidget(self.game_logo)
        hortizontal_layout_logo.addStretch()

        hortizontal_layout_btn = QtWidgets.QHBoxLayout()
        hortizontal_layout_btn.addStretch()
        hortizontal_layout_btn.addWidget(self.start_btn)
        hortizontal_layout_btn.addStretch()

        total_layout = QtWidgets.QVBoxLayout()
        total_layout.addStretch()
        total_layout.addLayout(hortizontal_layout_logo)
        total_layout.addStretch()
        total_layout.addLayout(hortizontal_layout_btn)
        total_layout.addStretch()

        self.setLayout(total_layout)
