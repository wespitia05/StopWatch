# python pyqt5 stopwatch

# provides modules used and maintained by the python interpreter
import sys
# provides gui components
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
# provides functionality
from PyQt5.QtCore import QTimer, QTime, Qt

# this class inherits from base class QWidget
class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        # create our time object, passes arguments: hours, minutes, seconds, milliseconds
        self.time = QTime(0, 0, 0, 0)
        # creates our label for the time object with the following format
        self.time_label = QLabel("00:00:00.00")
        # creates our start button
        self.start_button = QPushButton("Start", self)
        # creates our stop button
        self.stop_button = QPushButton("Stop", self)
        # creates our reset button
        self.reset_button = QPushButton("Reset", self)
        # adds timer to the clock
        self.timer = QTimer(self)
        self.initUI()
    
    # this is where we will be designing the user interface
    def initUI(self):
        # changes name of window title
        self.setWindowTitle("Stopwatch")

        # declares vbox will have a vertical box layout
        vbox = QVBoxLayout()
        # adds our widget to the vbox (time label)
        vbox.addWidget(self.time_label)

        # passes in our vertical layout manager to set as the layout
        self.setLayout(vbox)

        # gets our time label and centers it vetically/horizontally
        self.time_label.setAlignment(Qt.AlignCenter)

        # declares hbox will have a horizontal box layout
        hbox = QHBoxLayout()
        # adds our widgeta to the hbox (buttons)
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        # adds group of buttons in hbox to the vbox
        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton, QLabel {
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton {
                color: black;
                font-size: 50px;
                background-color: hsl(44, 4%, 79%);
                border-radius: 20px
            }   
            QLabel {
                color: black;
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
            }                 
        """)

        # connects our buttons to its specific function
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        # connects our timer update to its specific function
        self.timer.timeout.connect(self.update_display)

    # this function will handle starting the time
    def start(self):
        self.timer.start(10)

    # this function will handle stopping the time
    def stop(self):
        self.timer.stop()

    # this function will handle resetting the time
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    # this function will handle formatting the time
    def format_time(self, time):
        # creates our variables using time
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10 # converts milliseconds from 3 digits to 2
        # uses format specifier for 2 leading zeros
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    # this function will handle updating the time displayed
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app  = QApplication(sys.argv)
    # construct our stopwatch object
    stopwatch = Stopwatch()
    # show our stopwatch object
    stopwatch.show()
    # stopwatch object remains visible until exited
    sys.exit(app.exec_())