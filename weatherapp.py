import requests
import json
import tkinter as tk

# Create the GUI
root = tk.Tk()
root.geometry("400x200")
root.title("Weather App")

# Define the API key and base URL
api_key = "YOUR_API_KEY_HERE"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Define the function to retrieve weather data
def get_weather():
    # Retrieve the user's location from the entry box
    location = location_entry.get()

    # Construct the API URL
    complete_url = base_url + "appid=" + api_key + "&q=" + location

    # Send the HTTP request and get the response
    response = requests.get(complete_url)

    # Parse the response as JSON
    data = json.loads(response.text)

    # Extract the relevant weather data from the JSON
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    # Display the weather data in the GUI
    weather_label.config(text=f"Temperature: {temperature}\nHumidity: {humidity}\nWind Speed: {wind_speed}\nDescription: {description}")

# Create the location entry box and button
location_label = tk.Label(root, text="Enter location:")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

# Create the label to display the weather data
weather_label = tk.Label(root, text="")
weather_label.pack()

# Start the GUI
root.mainloop()