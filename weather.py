import requests

API_KEY = "46c1a43efdc6b9047e01d40f2d799850"  # You can get a free API key from openweathermap.org
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather():
    city = "Mangalore"
    complete_url = f"{BASE_URL}q={city}&appid={API_KEY}"
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        return f"The weather in {city} is {weather_desc} with a temperature of {main['temp']}°C."
    else:
        return "City not found."

