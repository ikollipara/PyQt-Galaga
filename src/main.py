# src/main.py
# Ian Kollipara
# 2020.03.12
# Main file for Atario
#
# Usage
# python3 src/main.py
# OR
# ./atario

# Imports
from PyQt5 import QtWidgets
from sys import argv, exit
from main_window import Main_Window


def main():
    PyQT_App = QtWidgets.QApplication(argv)
    Atario = Main_Window(PyQT_App)
    Atario.show()
    exit_condition = PyQT_App.exec_()
    exit(exit_condition)


main()
