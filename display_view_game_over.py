from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia

class GameOver(QtWidgets.QWidget):
    def __init__(self, controller, parent=None):
        super(GameOver, self).__init__(parent)
        self.background = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32)
        self.background.fill(QtGui.QColor('#000000'))
        self.GameOver = QtWidgets.QLabel(self)
        self.GameOver.setPixmap(QtGui.QPixmap('.\Images\Game Over.PNG'))
        self.controller = controller
        self.NameBox = QtWidgets.QLineEdit(self)
        self.highScore = QtWidgets.QLabel()
        self.highScore.setText(self.controller.ship.time)
        self.setup_layout()
        self.update()


    def setup_layout(self):
        vLayout = QtWidgets.QVBoxLayout()
        hLayoutOne = QtWidgets.QHBoxLayout()
        hLayoutTwo = QtWidgets.QHBoxLayout()
        hLayoutOne.addStretch()
        hLayoutOne.addWidget(self.GameOver)
        hLayoutOne.addStretch()
        hLayoutTwo.addWidget(self.NameBox)
        hLayoutTwo.addWidget(self.highScore)
        vLayout.addLayout(hLayoutOne)
        vLayout.addLayout(hLayoutTwo)
        self.setLayout(vLayout)

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)
        size = self.size()
        self.background = self.background.scaled(size)
        painter.drawImage(0, 0, self.background)





