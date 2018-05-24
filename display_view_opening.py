from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia

class Opening(QtWidgets.QWidget):
    def __init__(self, controller, parent=None):
        super(Opening, self).__init__(parent)
        self.controller = controller
        self.background = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32)
        self.background.fill(QtGui.QColor('#000000'))
        self.init_widgets()
        self.setup_layout()
        self.go = False
        self.update()

    def init_widgets(self):
        self.Logo = QtWidgets.QLabel()
        self.Logo.setPixmap(QtGui.QPixmap('.\Images\Logo.PNG'))
        self.start = QtWidgets.QPushButton()
        self.start.setText('Start')
        self.start.clicked.connect(self.startGame)



    def setup_layout(self):
        hLayoutOne = QtWidgets.QHBoxLayout()
        hLayoutOne.addStretch()
        hLayoutOne.addWidget(self.Logo)
        hLayoutOne.addStretch()
        hLayoutTwo = QtWidgets.QHBoxLayout()
        hLayoutTwo.addStretch()
        hLayoutTwo.addWidget(self.start)
        hLayoutTwo.addStretch()
        layout = QtWidgets.QVBoxLayout()
        layout.addStretch()
        layout.addLayout(hLayoutOne)
        layout.addStretch()
        layout.addLayout(hLayoutTwo)
        layout.addStretch()
        self.setLayout(layout)

    def startGame(self):
        self.go = True