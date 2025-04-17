# import function from file weather-tool.py
from weather_tool import get_weather

if __name__ == "__main__":
    latitude = 13.764902 
    longitude = 100.538331
    weather = get_weather(latitude, longitude)
    print(f"The current temperature is {weather}°C")