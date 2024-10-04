import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget

from widget_def import on_button_press, get_weather

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("Weather Tracker")

input_box = QLineEdit("")
input_box.setPlaceholderText("City:")

button = QPushButton("Find the weather")
button.clicked.connect(lambda: on_button_press(input_box))

weather_text = get_weather("Fremont", "API_KEY")
text = QLabel(f"{weather_text}")

layout = QVBoxLayout()
layout.addWidget(input_box)
layout.addWidget(button)
layout.addWidget(text)

window.setLayout(layout)

# get_weather("Fremont", "6f22d45461ea6663513d9f479a0317af")

window.show()

app.exec() 


# window: 
# input field for the city 
# button to search
# labels / textboxes / to display weather data

# api call 