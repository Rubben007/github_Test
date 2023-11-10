import requests

def weather_app(city):
    api_key = "85271fde01a7ec1e48b83d4e8d6e6a22"
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    data = response.json()
    return data 

def display_weather():
    city = input("Enter the city name: ").lower()
    weather_info = weather_app(city)
    
    if weather_info["cod"] == 200:
        temperature = weather_info["main"]["temp"]
        pressure = weather_info["main"]["pressure"]
        humidity = weather_info["main"]["humidity"]
        visibility = weather_info["visibility"]
        return f"temperature {temperature} degree celcius\npressure {pressure} pa\nhumidity {humidity} %rh\nvisibility {visibility} lumen(lm)"
    else:
        return "city not found"


data = display_weather()
print(data)

