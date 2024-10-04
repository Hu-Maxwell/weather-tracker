import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget



app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("Weather Tracker")

button = QPushButton("Find the weather")
input_box = QLineEdit("City: ")
text = QLabel("placeholder text")

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(input_box)
layout.addWidget(text)

window.setLayout(layout)

window.show()

app.exec() 


# window: 
# input field for the city 
# button to search
# labels / textboxes / to display weather data

# api call 