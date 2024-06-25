import requests
import json
def get_user_location():
    user_location = input("Enter the location for weather information: ")
    return user_location

def fetch_weather(location, api_key):
    #API URL
    api = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }

    #request get
    try:
        result = requests.get(api, params=params)
        result.raise_for_status()
        weather_data = result.json()
        return weather_data
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(weather_data):
    try:
        location = weather_data['name']
        country = weather_data['sys']['country']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        desctription = weather_data['weather'][0]['description']

        print(f"Weather in {location}, {country}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {desctription.capitalize()}")
    except KeyError as e:
        print(f"Error extracting weather data: {e}")

        
api_key = "cea480f592567920fdcda69d9aba4577"
location = get_user_location()
weather_data = fetch_weather(location, api_key)
print(f"Location entered: {location}")

if weather_data:
    display_weather(weather_data)