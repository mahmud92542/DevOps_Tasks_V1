from flask import Flask, jsonify
import socket
from datetime import datetime
import requests

app = Flask(__name__)

# Replace with your weather API key and URL
WEATHER_API_KEY = ""
WEATHER_API_URL = ""

@app.route('/api/weather')
def weather():
    hostname = socket.gethostname()
    current_datetime = datetime.now().strftime("%y%m%d%H%M")
    version = "1.0"  # Replace with your application version

    # Get weather data for Dhaka from the free weather API
    weather_data = get_weather_data("Dhaka")

    response_data = {
        "hostname": hostname,
        "datetime": current_datetime,
        "version": version,
        "weather": weather_data
    }

    return jsonify(response_data)

@app.route('/health')
def health_check():
    return "OK"

def get_weather_data(city):
    params = {
        "key": WEATHER_API_KEY,
        "q": city
    }
    response = requests.get(WEATHER_API_URL, params=params)
    data = response.json()

    # Extract relevant weather information
    temperature = data["main"]["temp"]
    temp_unit = "c"

    return {
        "temperature": temperature,
        "temp_unit": temp_unit
    }

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
