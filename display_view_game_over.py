from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia

class GameOver(QtWidgets.QWidget):
    def __init__(self, controller, parent=None):
        super(GameOver, self).__init__(parent)
        self.controller = controller
        self.background = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32)
        self.init_widgets()
        self.setup_layout()

    def init_widgets(self):
        self.gameOver = QtWidgets.QLabel()
        self.gameOver.setPixmap(QtGui.QPixmap('.\Images\Game Over.PNG'))
        self.highScore = QtWidgets.QLabel()
        self.highScore.setText(self.controller.ship.time)
        self.highScore.setAlignment(QtCore.Qt.AlignCenter)
        self.NameBox = QtWidgets.QLineEdit()
        self.NameBoxText = QtWidgets.QLabel()
        self.NameBoxText.setText('Please enter in your Name')
        self.NameBoxText.setAlignment(QtCore.Qt.AlignCenter)
        self.highScoreText = QtWidgets.QLabel()
        self.highScoreText.setText('Your Time')

    def setup_layout(self):
        hBoxTop = QtWidgets.QHBoxLayout()
        hBoxBottom = QtWidgets.QHBoxLayout()
        vBoxTotal = QtWidgets.QVBoxLayout()
        vBoxBottomLeft = QtWidgets.QVBoxLayout()
        vBoxBottomRight = QtWidgets.QVBoxLayout()
        hBoxTop.addStretch()
        hBoxTop.addWidget(self.gameOver)
        hBoxTop.addStretch()
        vBoxBottomLeft.addStretch()
        vBoxBottomLeft.addWidget(self.highScoreText)
        vBoxBottomLeft.addWidget(self.highScore)
        vBoxBottomLeft.addStretch()
        vBoxBottomRight.addStretch()
        vBoxBottomRight.addWidget(self.NameBoxText)
        vBoxBottomRight.addWidget(self.NameBox)
        vBoxBottomRight.addStretch()
        hBoxBottom.addStretch()
        hBoxBottom.addLayout(vBoxBottomLeft)
        hBoxBottom.addStretch()
        hBoxBottom.addLayout(vBoxBottomRight)
        hBoxBottom.addStretch()
        vBoxTotal.addStretch()
        vBoxTotal.addLayout(hBoxTop)
        vBoxTotal.addStretch()
        vBoxTotal.addLayout(hBoxBottom)
        vBoxTotal.addStretch()
        self.setLayout(vBoxTotal)

    def create_score(self):
        counter = 0
        playerName = self.NameBox.text()
        score = self.controller.ship.time
        if ':' in score:
            testScore = score.split(':')
            testScore = int(str(testScore[0]) + str(testScore[1]))
        else: testScore = score
        testTimes, times, names = self.get_score()
        for time in testTimes:
            if testScore > int(time):
                index = counter
                break
            else: counter += 1
        names.insert(index, playerName)
        times.insert(index, score)
        self.add_scores(names, times)

    def get_score(self):
        times = []
        testTimes = []
        names = []
        with open('HighScores', 'r') as f:
            for line in f:
                name, time, n = line.split(',')
                if ':' in time:
                    testTime = time.split(':')
                    testTime = int(str(testTime[0]) + str(testTime[1]))
                else: testTime = int(time)
                names.append(name)
                times.append(time)
                testTimes.append(testTime)
        return testTimes, times, names

    def add_scores(self, names, times):
        string = ''
        counter = 0
        for name in names:
            string += '{},{},\n'.format(name, times[counter])
            counter += 1
        with open('HighScores', 'w') as f:
            f.write(string)