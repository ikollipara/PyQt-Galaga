# src/main_window.py
# Ian Kollipara
# 2020.03.12
# Main Instance of Atario
#
# Usage
# from main_window import Main_Window

# Imports
from PyQt5 import QtGui, QtCore, QtWidgets
from controller.controller import Controller
from view.main_screen import Main_Screen

# Constants
DEFAULT_WINDOW_SIZE = (1000, 900)


class Main_Window(QtWidgets.QMainWindow):
    """ Main Window Instance for Atario. 

    Uses a MVC style architecture. 
    """

    resized = QtCore.pyqtSignal()

    # Instance Variables (private)
    # app         QApplication instance
    # controller  Main Application Controller
    # display     Central Widget for Main_Window

    def __init__(self, app: QtWidgets.QApplication):
        """ __init__() create Main_Window object. 

        Parameters
        app  QApplication Instance
        """

        super(Main_Window, self).__init__()
        self.app = app
        self.controller = Controller()

        # Initialization functions
        self._setup_window()
        self._set_display(Controller().get_current_screen())
        self._create_menu()
        self._setup_status_bar()
        self._start_instance_timer()

        self.resized.connect(self.update_screen_size)

    def update_screen_size(self) -> None:
        self.controller.update_screen_size(
            self.display.width(), self.display.height())

    def _set_display(self, cls) -> None:
        """ Set Central Widget to given class. 

        Parameters
        cls  Class type from view
        """

        self.display = cls(self.controller)
        self.setCentralWidget(self.display)
        self.display.show()

    def _setup_window(self) -> None:
        """ Setup default window. """

        self.resize(DEFAULT_WINDOW_SIZE[0], DEFAULT_WINDOW_SIZE[1])

        # Center Instance in the middle of the screen
        desktop_size = QtWidgets.QDesktopWidget().screenGeometry()
        window_size = self.geometry()
        self.move((desktop_size.width() - window_size.width())/2,
                  (desktop_size.height() - window_size.height())/2)

        self.setWindowTitle("Atario")
        self.setWindowIcon(QtGui.QIcon("src/images/Window Icon.jpg"))

    def _create_menu(self) -> None:
        """ Create window menu bar. """

        about = QtWidgets.QAction(
            "&About", self, statusTip="More Info about the Program", triggered=self.about)
        self.menuBar().addAction(about)

    def about(self) -> None:
        QtWidgets.QMessageBox.about(
            self, "Atario", "This Program was orginally developed by Ian Kollipara, Tessa Brazda, and Collin Rich over the course of 3 weeks. It was later rewritten by Ian Kollipara.")

    def _setup_status_bar(self) -> None:
        """ Setup window status bar. """

        # Don't create status bar when
        # self.display isn't the game widget
        if isinstance(self.display, Main_Screen):
            time = self.controller.get_time()
            self.statusBar().showMessage(
                f"Lives: {self.controller.get_ship_lives()} | Time: {time}")

    def _start_instance_timer(self) -> None:
        """ Create overall instance timer. """

        self.instance_timer = QtCore.QTimer()
        self.instance_timer.timeout.connect(self._setup_status_bar)
        self.instance_timer.timeout.connect(self.load_current_screen)
        self.instance_timer.timeout.connect(self.update)
        self.instance_timer.start(10)

    def load_current_screen(self) -> None:
        if not isinstance(self.display, self.controller.get_current_screen()):
            self._set_display(self.controller.get_current_screen())

    def resizeEvent(self, event):
        self.resized.emit()
        return super(Main_Window, self).resizeEvent(event)

    def keyPressEvent(self, QKeyEvent):
        key = QKeyEvent.key()

        if key in [QtCore.Qt.Key_D, QtCore.Qt.Key_Right]:
            self.controller.update_ship_location("right")

        elif key in [QtCore.Qt.Key_A, QtCore.Qt.Key_Left]:
            self.controller.update_ship_location("left")

        elif key in [QtCore.Qt.Key_W, QtCore.Qt.Key_Up]:
            self.controller.update_ship_location("up")

        elif key in [QtCore.Qt.Key_S, QtCore.Qt.Key_Down]:
            self.controller.update_ship_location("down")
