import requests
import tkinter as tk
from PIL import Image, ImageTk

def get_weather_and_image(city):
    api_key = "85aab7f0e02be432c20c60fc5c1a6449"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description'].lower()
        temp = data['main']['temp']
        
        if "clear" in weather:
            image_path = "weather/sun.png"
        elif "partly" in weather or "few clouds" in weather:
            image_path = "weather/cloudy.png"
        elif "cloud" in weather:
            image_path = "weather/cloudy.png"
        elif "rain" in weather:
            image_path = "weather/rainy.png"
        elif "storm" in weather or "thunderstorm" in weather:
            image_path = "weather/storm.png"
        elif "snow" in weather:
            image_path = "weather/snowflake.png"
        elif "wind" in weather or "breeze" in weather:
            image_path = "weather/windy.png"
        elif "fog" in weather or "mist" in weather:
            image_path = "weather/foggy.png"
        elif "cold" in weather:
            image_path = "weather/snowflake.png"
        elif "hot" in weather:
            image_path = "weather/hot.png"
        elif "sleet" in weather:
            image_path = "weather/sleet.png"
        elif "hail" in weather:
            image_path = "weather/hail.png"
        elif "humid" in weather:
            image_path = "weather/humid.png"
        elif "haze" in weather or "hazy" in weather:
            image_path = "weather/hazy.png"
        else:
            image_path = "weather/unknown.png"  # Default image for unknown weather

        return f"{weather.capitalize()} {temp}°C", image_path
    else:
        return "Error: Unable to fetch the weather information.", ""

def weather():
    city_name = entry.get()
    weath, image_path = get_weather_and_image(city_name)
    descri.set(weath)
    
    try:
        img = Image.open(image_path)
        img = img.resize((100, 100), Image.ANTIALIAS)  # Resize image as needed
        photo = ImageTk.PhotoImage(img)
        label2.config(image=photo)
        label2.image = photo  # Keep a reference to avoid garbage collection
    except Exception as e:
        print(f"Error: Unable to open image at {image_path} - {e}")
        label2.config(image="")  # Clear the label if there's an error

# GUI setup
root = tk.Tk()
root.title("Weather App")

# Configure the grid layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Entry widget to input the city name
entry = tk.Entry(root)
entry.grid(row=0, column=0, pady=10)

# Button to trigger the weather function
button = tk.Button(root, text="Get Weather", command=weather)
button.grid(row=1, column=0, pady=10)

descri = tk.StringVar()
label1 = tk.Label(root, textvariable=descri)
label1.grid(row=2, column=0, pady=10)

label2 = tk.Label(root)
label2.grid(row=3, column=0, pady=20)

root.mainloop()
