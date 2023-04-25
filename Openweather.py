import requests
from datetime import datetime

api_key = "9f6aacdb612de2bec6b25fa520ed5331"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name: ")
units = "metric"  # Use "imperial" for Fahrenheit

complete_url = f"{base_url}appid={api_key}&q={city_name}&units={units}"

response = requests.get(complete_url)

if response.status_code == 200:
    data = response.json()
    main_data = data["main"]
    temperature = main_data["temp"]
    weather_data = data["weather"]
    weather_description = weather_data[0]["description"]

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d/%m/%Y")

    print("--------------------------------------------------")
    print(f"Weather report for {city_name} as of {current_time} on {current_date}")
    print("--------------------------------------------------")
    print(f"Temperature: {temperature}°C")
    print(f"Weather Description: {weather_description.capitalize()}")
    print("--------------------------------------------------")
else:
    print("Error: City not found!")
