# window: 
# input field for the city 
# button to search
# labels / textboxes / to display weather data

# api call 


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget


# a main window needs a central widget, and you can give the central widget a layout
# 1. create the widgets
# 2. create and set the layout
# 3. create and set the central widget
# 4. set QMainWindow's central widget
class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather Tracker")
        self.button = QPushButton("Find the weather")
        self.city = QLineEdit("Enter your city here:")
        self.text = QLabel("placeholder text")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.city)
        self.layout.addWidget(self.text)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)

        self.setCentralWidget(central_widget)

app = QApplication(sys.argv)

window = MainWindow() 
window.show()

app.exec() 
