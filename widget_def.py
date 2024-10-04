import requests

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
        return 

def handle_button_press(input_box, label): 
    api_key = "key"
    city_name = on_button_press(input_box)
    weather_data = get_weather(city_name, api_key)

    label.setText(weather_data)
