import requests
import os

def on_button_press(input_box): 
    city_name = input_box.text()
    return city_name


def get_weather(city_name, api_key): 
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': "metric"
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200: 
        data = response.json()
        main = data['main']

        temp = "Temp: " + str(main['temp']) + "\n"
        wind = "Wind speed: " + str(data['wind']['speed']) + "\n"
        humidity = "Humidity: " + str(main['humidity']) + "\n"
        weather_description = "Weather description: " + str(data['weather'][0]['main']) + "\n"

        return temp + humidity + wind + weather_description
    else: 
        if response.status_code == 404: 
            return "City not found."
        else: 
            return "An error occured."

def handle_button_press(input_box, label): 
    api_key = os.getenv('WEATHER_API_KEY')
    city_name = on_button_press(input_box)
    weather_data = get_weather(city_name, api_key)

    if weather_data:
        label.setText(weather_data)
    else: 
        label.setText("Invalid city!")