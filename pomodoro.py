import sys
from PyQt5.QtWidgets import (QApplication,QWidget,
                             QPushButton, QVBoxLayout,
                             QHBoxLayout) 

from PyQt5.QtCore import QTimer, QTime, Qt

from PyQt5.QtGui import QIcon

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Own Pomodoro')
        self.setWindowIcon(QIcon("clock.png"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())





