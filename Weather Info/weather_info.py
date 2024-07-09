import json
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

def create_main_window():
    window = tk.Tk()
    window.geometry("450x500")
    window.title("Weather Application")
    
    def get_weather():
        location = location_entry.get()
        if location:
            weather_data = fetch_weather(location, api_key)
            
            if weather_data:
                display_weather(weather_data, weather_info, weather_icon_label)
                forecast_data = fetch_forecast(location, api_key)
                if forecast_data:
                    display_forecast(forecast_data, forecast_info)
                else:
                    messagebox.showerror("Error", "Could not retrieve forecast data.")
            else:
                messagebox.showerror("Error", "Could not retrieve weather data.")
        else:
            messagebox.showerror("Input Required", "Please enter a location.")

    # Location input field
    tk.Label(window, text="Enter location:").pack(pady=5)  # widget 1
    location_entry = tk.Entry(window)
    location_entry.pack(pady=5)    # widget 2

    fetch_button = tk.Button(window, text="Get Weather", command=get_weather)
    fetch_button.pack(pady=10)    # widget 3

    # weather info field
    weather_info = tk.Label(window, text="", justify="left")
    weather_info.pack(pady=10) # widget 4

    weather_icon_label = tk.Label(window)
    weather_icon_label.pack(pady=10)    # widget 5

    forecast_info = tk.Label(window, text="", justify="left")
    forecast_info.pack(pady=10) # widget 6


    


    window.mainloop()

def fetch_weather(location, api_key):
    #API URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        result = requests.get(url, params=params)
        result.raise_for_status()
        weather_data = result.json()
        return weather_data
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def fetch_forecast(location, api_key):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        result = requests.get(url, params=params)
        result.raise_for_status()
        forecast_data = result.json()
        return forecast_data
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(weather_data, weather_info, weather_icon_label):
    try:
        location = weather_data['name']
        country = weather_data['sys']['country']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        desctription = weather_data['weather'][0]['description']
        icon_num = weather_data['weather'][0]['icon']

        weather_info.config(text=(
            f"Weather in {location}, {country}\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Description: {desctription.capitalize()}"
        ))

        # weather icon
        icon_url = f"https://openweathermap.org/img/wn/{icon_num}@2x.png"
        icon_result = requests.get(icon_url)
        icon_image = Image.open(io.BytesIO(icon_result.content))
        icon_photo = ImageTk.PhotoImage(icon_image)

        weather_icon_label.config(image=icon_photo)
        weather_icon_label.image = icon_photo # Prevent images from being removed by garbage collection.
    except KeyError as e:
        weather_info.config(text = f"Error extracting weather data: {e}")

def display_forecast(forecast_data, forecast_info):
    try:
        forecast_text = "5-day Forecast\n"
        for forecast in forecast_data["list"]:
            if "00:00:00" in forecast["dt_txt"]:
                date = forecast["dt_txt"].split(" ")[0]
                temp = forecast["main"]["temp"]
                description = forecast["weather"][0]["description"]
                forecast_text += f"{date} {temp}°C {description.capitalize()}\n"

        forecast_info.config(text = forecast_text)
    except KeyError as e:
        forecast_info.config(text = f"Error extracting weather data: {e}")



api_key = "own_API_key" # Change to the API key issued by OpenWeatherMap.

if __name__ == "__main__":
    create_main_window()