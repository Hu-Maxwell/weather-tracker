import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow): # QMainWindow is the superclass 
    def __init__(self): 
        super().__init__() # refers to the superclass and calls it's initializer (constructor)
        self.setWindowTitle("My App")

        button = QPushButton("Press me!")
        button.clicked.connect(self.on_click)

        self.setFixedSize(QSize(400, 300))

        self.setCentralWidget(button)
    
    def on_click(self): 
        print("Clicked!")

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
# signals can recieve data 
#   .clicked EMITS a SIGNAL
#   when clicked, it returns a signal (basically calling a function)
#   .connect(self.on_click) 
#   the signal calls the above code 