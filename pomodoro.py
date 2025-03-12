import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication,QWidget, QPushButton, QVBoxLayout,QHBoxLayout, QLabel, QLineEdit) 
from PyQt5.QtCore import QTimer, QTime, Qt

class Pomodoro(QWidget):
    def __init__(self):
        super(Pomodoro, self).__init__()

        self.title_label = QLabel("Consistency, Objective, Discipline:")
        self.input = QLineEdit(self)
        self.timer_label = QLabel ("00:00", self)
        self.start_button = QPushButton("Start", self)
        self.pause_button = QPushButton("Pause", self)
        self.restart_button = QPushButton("Restart", self)
        self.restart_time_total = QPushButton("Restart Time Spent", self)
        self.time_spent = QLabel("Time spent total: 00:00")

        self.time = QTime(0,0)
        self.time_total = QTime(0, 0)
        self.paused = False 
        self.started = QTimer(self)

        self.initUI()


    def initUI(self):
        
        self.setWindowTitle('My Own Pomodoro')

        ##LAYOUT
        box1 = QVBoxLayout()

        box1.addWidget(self.title_label)
        box1.addWidget(self.timer_label)
        box1.addWidget(self.input)
        box1.addWidget(self.time_spent)

        box2 = QHBoxLayout()

        box2.addWidget(self.start_button)
        box2.addWidget(self.pause_button)
        box2.addWidget(self.restart_button)
        box2.addWidget(self.restart_time_total)

        box1.addLayout(box2)
        self.setLayout(box1)

        ##STYLING
        self.timer_label.setAlignment(Qt.AlignCenter)

        self.title_label.setFont(QFont("Arial", 18, 18, False))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setFont(QFont("Arial", 20, 20, True))
        self.time_spent.setFont(QFont("Arial", 16, 16, False))
        self.input.setStyleSheet("""
        font-size: 14px;
        border: 2px solid;
        border-radius: 5px;
        padding: 5px;
        """)
        self.input.setContentsMargins(150, 0, 150, 0)
        self.input.setPlaceholderText("Enter minutes")
 
        #SIGNAL -> SLOTS
        self.start_button.clicked.connect(self.start)
        self.pause_button.clicked.connect(self.pause)
        self.restart_button.clicked.connect(self.restart)
        self.restart_time_total.clicked.connect(self.restart_time_spent)
        self.started.timeout.connect(self.time_out)


       
    def start(self):
        try:
            user_time = int(self.input.text())
            self.time = QTime(0, user_time, 0)
            self.timer_label.setText(self.time.toString("mm:ss"))
        except ValueError:
            self.timer_label.setText("Invalid input! Enter a integer number.")
            return
        self.started.start(1000)
        self.paused = False
                
    def pause(self):
        self.started.stop()
        self.paused = True

    def restart_time_spent(self):
        self.time_total = QTime(0, 0)
        self.time_spent.setText(f"Time spent total: {self.time_total.toString('mm:ss')}")

    def restart(self):
        self.started.stop()
        self.timer_label.setText("00:00")
        self.time_total = QTime(0, 0)
        self.time_spent.setText(f"Time spent total: {self.time_total.toString('mm:ss')}")
        

    def time_out(self):
            if self.time > QTime(0, 0):
                self.time = self.time.addSecs(-1) 
                self.timer_label.setText(self.time.toString("mm:ss"))

                self.time_total = self.time_total.addSecs(1) # Counting total
                self.time_spent.setText(f"Time spent total: {self.time_total.toString('mm:ss')}")
            else:
                 self.timer.stop()
                 self.time = QTime(0, 0)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    pomodoro = Pomodoro()
    pomodoro.show()
    sys.exit(app.exec_())





