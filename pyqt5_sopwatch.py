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
        pass

    # this function will handle starting the time
    def start(self):
        pass

    # this function will handle stopping the time
    def stop(self):
        pass

    # this function will handle resetting the time
    def reset(self):
        pass

    # this function will handle formatting the time
    def format_time(self, time):
        pass

    # this function will handle updating the time displayed
    def update_display(self):
        pass

if __name__ == "__main__":
    app  = QApplication(sys.argv)
    # construct our stopwatch object
    stopwatch = Stopwatch()
    # show our stopwatch object
    stopwatch.show()
    # stopwatch object remains visible until exited
    sys.exit(app.exec_)