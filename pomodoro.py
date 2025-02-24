import sys
from PyQt5.QtWidgets import (QApplication,QWidget,
                             QPushButton, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit) 

from PyQt5.QtCore import QTimer, QTime, Qt


class Pomodoro(QWidget):
    def __init__(self):
        super().__init__()

        self.title_label = QLabel("Consistency, Discipline, Objective:")
        self.input = QLineEdit(self)
        self.time_label = QLabel ("00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.time_spent = QLabel("Time spent total: ")

        self.time = QTime(0, 0)
        self.time_total = QTime(0, 0)

        self.timer = QTimer(self)

        self.initUI()


    def initUI(self):
        
        self.setWindowTitle('My Own Pomodoro')

        box1 = QVBoxLayout()

        box1.addWidget(self.title_label)
        box1.addWidget(self.input)
        box1.addWidget(self.time_label)
        box1.addWidget(self.time_spent)

        box2 = QHBoxLayout()

        box2.addWidget(self.start_button)
        box2.addWidget(self.stop_button)

        box1.addLayout(box2)
        self.setLayout(box1)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.input.setPlaceholderText("Enter time in minutes")

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.timer.timeout.connect(self.time_out)

       
    def start(self):

        try:
                user_time = int(self.input.text())
                self.time = QTime(0, user_time, 0)
                self.time_label.setText(self.time.toString("mm:ss"))
                self.timer.start(1000)
        except ValueError:
            self.time_label.setText("Invalid input! Enter a number.")

    def stop(self):
        self.timer.stop()

  
    def format(self, time):
        minutos = time.minute()
        segundos = time.seconds()
        return f"{minutos:02}:{segundos:02}"

    def time_out(self):
            if self.time > QTime(0, 0):
                self.time = self.time.addSecs(-1)  # Decrease time by 1 second
                self.time_label.setText(self.time.toString("mm:ss"))

                self.time_total = self.time_total.addSecs(1)
                self.time_spent.setText(f"Total Time Spent: {self.time_total.toString('mm:ss')}")
            else:
                 self.timer.stop()
                 self.time_label.setText('Time its over!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pomodoro = Pomodoro()
    pomodoro.show()
    sys.exit(app.exec_())





