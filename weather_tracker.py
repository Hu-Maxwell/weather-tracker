import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget

from widget_def import handle_button_press

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("Weather Tracker")

input_box = QLineEdit("")
input_box.setPlaceholderText("City:")

button = QPushButton("Find the weather")

text = QLabel("Weather data will appear here.")

layout = QVBoxLayout()
layout.addWidget(input_box)
layout.addWidget(button)
layout.addWidget(text)

button.clicked.connect(lambda: handle_button_press(input_box, text))


window.setLayout(layout)

window.show()

app.exec() 