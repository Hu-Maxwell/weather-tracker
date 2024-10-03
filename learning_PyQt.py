import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# app is now a QApplication object. a QApplication object handles:
#   initialization of GUI
#   the main loop
#   event handling
#
# could also be QApplication([]) if commmand line stuff isn't needed

app = QApplication(sys.argv)

# QWidget !!
#   Qwidgets are a base class for everything, and all other GUI elements inherit from
#   window = QWidget() 
#   QWidget() returns a window

# QMainWindow
window = QMainWindow()

window.show()  
app.exec() 
