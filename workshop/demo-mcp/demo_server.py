from fastmcp import FastMCP
import requests

mcp = FastMCP("MCP get weather by location",
              description="MCP get weather by location (lat, lon)",
              host="127.0.0.1",
              port=8080,
              log_level="DEBUG",
              timeout=30)

@mcp.tool()
def get_weather(latitude, longitude):
    print(f"Getting weather for {latitude}, {longitude}")
    # Write log file
    with open("weather_log.txt", "a") as log_file:
        log_file.write(f"Getting weather for {latitude}, {longitude}\n")
    # Example API call to Open-Meteo
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return f'Temperature: {data["current"]["temperature_2m"]}°C'

if __name__ == "__main__":
    mcp.run()