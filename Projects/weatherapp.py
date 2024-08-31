import requests
import tkinter as tk

def get_weather(city):
    # Replace with your API key
    api_key = "85aab7f0e02be432c20c60fc5c1a6449"
    # Base URL and endpoint
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    # Parameters for the API request
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use 'imperial' for Fahrenheit
    }
    
    # Make the request to the API
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data returned by the API
        data = response.json()
        # Extract the relevant information
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"{weather} {temp}°C"
    else:
        # Handle errors (e.g., invalid city name, issues with the API)
        return "Error: Unable to fetch the weather information."

def get_symbole(city):
    # Replace with your API key
    api_key = "85aab7f0e02be432c20c60fc5c1a6449"
    # Base URL and endpoint
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    # Parameters for the API request
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use 'imperial' for Fahrenheit
    }
    
    # Make the request to the API
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data returned by the API
        data = response.json()
        # Extract the relevant information
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        
        if "clear sky" in weather:
            return "☀️"
        elif "partly" in weather or "few clouds" in weather:
            return  "🌤️"
        elif "cloud" in weather:
            return  "☁️"
        elif "rain" in weather:
            return  "🌧️"
        elif "storm" in weather or "thunderstorm" in weather:
            return "⛈️"
        elif "snow" in weather:
            return  "❄️"
        elif "wind" in weather or "breeze" in weather:
            return  "🌬️"
        elif "fog" in weather or "mist" in weather:
            return  "🌫️"
        elif "cold" in weather:
            return  "❄️"
        elif "hot" in weather:
            return  "🌡️"
        elif "sleet" in weather:
            return  "🌨️"
        elif "hail" in weather:
            return  "🌨️"
        elif "humid" in weather:
            return  "💦"
        elif "haze" in weather or "hazy" in weather:
            return  "🌁"
        else:
            return  "❓"
    else:
        # Handle errors (e.g., invalid city name, issues with the API)
        return "Error: Unable to fetch the weather information."    


def weather():
  city_name=entry.get()
  weath=get_weather(city_name)
  weather=get_symbole(city_name)
  descri.set(weath)
  descri2.set(weather)

window=tk.Tk()
window.title("WEATHER APP")
window.geometry("500x500")
window.config(bg="black")

window_label=tk.Label(window,text="WEATHER_APP",bg="black",fg="white",font="calibri 15 bold")
window_label.pack()

window_frame=tk.Frame(window,bg='black')
window_frame.pack()

description_label=tk.Label(window_frame,text="Enter a city name",bg="black",fg="white",font="calibri 13 bold")
description_label.pack(pady=5)

entry=tk.StringVar()
entry1=tk.Entry(window_frame,width=30,textvariable=entry)
entry1.pack(pady=5)

button=tk.Button(window_frame,text="Get Weather",bg='black',fg='white',width=11,font='calibri 10 bold',command=weather)
button.pack(pady=5,)

descri=tk.StringVar()
descri_label=tk.Label(window,text="",bg='black',fg='white',font='calibri 14 bold',textvariable=descri)
descri_label.pack(pady=5)

descri2=tk.StringVar()
descri2_label=tk.Label(window,text="",bg="black",fg="white",font='calibri 40 bold',anchor="center",justify="center",textvariable=descri2)
descri2_label.pack(pady=10)
window.mainloop()
