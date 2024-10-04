import requests

def on_button_press(input_box): 
    input_text = input_box.text()
    print(f"{input_text}")


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

        temp = main['sea_level']

        return temp
    else: 
        return 
