from PyQt5 import QtWidgets
import sys
from Controller import Controller
from display_interface import GameWindow

def main():
    pyQTApp = QtWidgets.QApplication(sys.argv)
    Atario = GameWindow(pyQTApp)
    print(Atario.width())
    print(Atario.height())
    Atario.show()
    exitCondition = pyQTApp.exec_()
    sys.exit(exitCondition)

main()