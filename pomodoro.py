import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication,QWidget, QPushButton, QVBoxLayout,QHBoxLayout, QLabel, QLineEdit) 
from PyQt5.QtCore import QTimer, QTime, Qt

class Pomodoro(QWidget):
    def __init__(self):
        super(Pomodoro, self).__init__()

        self.title_label = QLabel("Consistency, Objective, Discipline:")
        self.input = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.timer_label = QLabel ("00:00", self)
        self.break_label = QLabel ("00:00", self)
        self.start_button = QPushButton("STUDY!", self)
        self.pause_button = QPushButton("Pause", self)
        self.restart_button = QPushButton("Restart", self)
        self.break_button = QPushButton("Break!!", self)
        self.time_spent = QLabel("Time spent studying: 00:00")
        self.break_spent = QLabel("Time spent in break: 00:00")

        self.time = QTime(0,0)
        self.time_total = QTime(0, 0, 0)
        self.break_time = QTime(0,0)
        self.break_total = QTime(0, 0, 0)
        self.started = QTimer(self)
        self.break_started = QTimer(self)
        self.paused = False 
        self.isBreak = False

        self.initUI()


    def initUI(self):
        
        self.setWindowTitle('My Own Pomodoro')

        ##LAYOUT
        box1 = QVBoxLayout()

        box1.addWidget(self.title_label)
        box1.addWidget(self.timer_label)
        box1.addWidget(self.input)
        box1.addWidget(self.break_label)
        box1.addWidget(self.input2)
        box1.addWidget(self.time_spent)
        box1.addWidget(self.break_spent)

        box2 = QHBoxLayout()

        box2.addWidget(self.start_button)
        box2.addWidget(self.pause_button)
        box2.addWidget(self.restart_button)
        box2.addWidget(self.break_button) 

        box1.addLayout(box2)
        self.setLayout(box1)

        ##STYLING
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.break_label.setAlignment(Qt.AlignCenter)

        self.title_label.setFont(QFont("Arial", 18, 18, False))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setFont(QFont("Arial", 20, 20, True))
        self.break_label.setFont(QFont("Arial", 20, 20, True))
        self.time_spent.setFont(QFont("Arial", 16, 16, False))
        self.break_spent.setFont(QFont("Arial", 16, 16, False))
        
        self.input.setStyleSheet(
        """
        font-size: 14px;
        border: 2px solid;
        border-radius: 5px;
        padding: 5px;
        """)
        self.input.setContentsMargins(150, 0, 150, 0)
        self.input.setPlaceholderText("STUDY!")

        self.input2.setStyleSheet(
        """
        font-size: 14px;
        border: 2px solid;
        border-radius: 5px;
        padding: 5px;
        """)
        self.input2.setContentsMargins(150, 0, 150, 0)
        self.input2.setPlaceholderText("BREAK")
 
        #SIGNAL -> SLOTS
        self.start_button.clicked.connect(self.start)
        self.pause_button.clicked.connect(self.pause)
        self.restart_button.clicked.connect(self.restart)
        self.break_button.clicked.connect(self.start_break)
        self.started.timeout.connect(self.time_out)
        self.break_started.timeout.connect(self.time_out2)


       
    def start(self):
        if not self.paused:
            try:
                user_time = int(self.input.text())
                self.time = QTime(0, user_time, 0)
                self.timer_label.setText(self.time.toString("mm:ss"))
            except ValueError:
                self.timer_label.setText("Invalid input! Enter a integer number.")
                self.time = QTime(0, 0)
                return
        self.started.start(1000)
        self.paused = False

                
    def pause(self):

            self.started.stop()
            self.paused = True
            self.break_started.stop()
            self.isBreak = True


    def restart(self):
        self.started.stop()
        self.timer_label.setText("00:00")
        self.time = QTime(0, 0)
        self.break_started.stop()
        self.break_label.setText("00:00")
        self.break_time = QTime(0, 0)
       
    def start_break(self):
        if not self.isBreak:
            try:
                user_time = int(self.input2.text())
                self.break_time = QTime(0, user_time, 0)
                self.break_label.setText(self.break_time.toString("mm:ss"))
            except ValueError:
                self.break_label.setText("Invalid input! Enter a integer number.")
                self.break_time = QTime(0, 0)
                return
        self.break_started.start(1000)
        self.isBreak = False

    def time_out(self):
            if self.time > QTime(0, 0):
                self.time = self.time.addSecs(-1) 
                self.timer_label.setText(self.time.toString("mm:ss"))

                self.time_total = self.time_total.addSecs(1) # Counting total
                self.time_spent.setText(f"Time spent studying: {self.time_total.toString('hh:mm:ss')}")
            else:
                 self.started.stop()
                 self.paused = False
                 self.time = QTime(0, 0)
    
    
    def time_out2(self):
            if self.break_time > QTime(0, 0):
                self.break_time = self.break_time.addSecs(-1) 
                self.break_label.setText(self.break_time.toString("mm:ss"))

                self.break_total = self.break_total.addSecs(1) # Counting total
                self.break_spent.setText(f"Time spent in break: {self.break_total.toString('hh:mm:ss')}")
            else:
                 self.break_started.stop()
                 self.paused = False
                 self.break_time = QTime(0, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pomodoro = Pomodoro()
    pomodoro.show()
    sys.exit(app.exec_())