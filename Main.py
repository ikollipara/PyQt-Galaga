from PyQt5 import QtWidgets
import sys
from Controller import Controller
from display_interface import GameWindow

def main():
    pyQTApp = QtWidgets.QApplication(sys.argv)
    Atario = GameWindow(pyQTApp)
    Atario.show()
    exitCondition = pyQTApp.exec_()
    sys.exit(exitCondition)

main()