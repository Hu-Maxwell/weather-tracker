import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow): # QMainWindow is the superclass 
    def __init__(self): 
        super().__init__() # refers to the superclass and calls it's initializer (constructor)
        self.setWindowTitle("My App")

        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.on_click)

        self.setCentralWidget(self.button)

    def on_click(self): 
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False) 
        self.setWindowTitle("My Oneshot App")


app = QApplication(sys.argv)

window = MainWindow() 
window.show()

app.exec() 


# app is now a QApplication object. a QApplication object handles:
#   initialization of GUI
#   the main loop
#   event handling
#
# could also be QApplication([]) if commmand line stuff isn't needed

# QWidget !!
#   Qwidgets are a base class for everything, and all other GUI elements inherit from
#   window = QWidget() 
#   QWidget() returns a window

# QMainWindow

# sending and recieving signals: 
# signals can emit data 
#   .clicked emits a signal
#   when clicked, it emits a signal (basically calling a function)
#   .connect(self.on_click) 
#   the signal calls the above code 

# button
#   whenever it's clicked, it emits emits a signal
#   when it is set to "checkable", the signal has a bool value
#   returns true when pressed, and false when released
#   
#   .setEnabled()
#   takes for input a bool val, and allows / disallows button from being clickable

# by writing self.button, you are making yourself capable of storing data from the button press, 
# because the button becomes part of the class as well, instead of just part of the window