from flask import Flask, jsonify
import socket, json, requests, boto3
from datetime import datetime

app = Flask(__name__)


# AWS region and secret name
AWS_REGION = 'ap-southeast-1'
SECRET_NAME = 'weatherApiKey'

secrets_manager = boto3.client('secretsmanager', region_name=AWS_REGION)

# Function to get secrets from AWS Secrets Manager
def get_secrets():
    try:
        response = secrets_manager.get_secret_value(SecretId=SECRET_NAME)
        secret_data = response.get('SecretString')
        if secret_data:
            return json.loads(secret_data)
        else:
            print("SecretString is not available. Trying to parse SecretBinary.")
            return json.loads(response['SecretBinary'].decode('utf-8'))
    except Exception as e:
        print(f"Error retrieving secrets: {e}")
        return None

# Retrieve secrets from AWS Secrets Manager
secrets = get_secrets()

# Check if secrets were successfully retrieved
if secrets is not None:
    # Update the API key and URL with the retrieved secrets
    WEATHER_API_KEY = secrets.get('WEATHER_API_KEY', '')
    WEATHER_API_URL = secrets.get('WEATHER_API_URL', '')
else:
    # Handle the case when secrets retrieval fails
    print("Secrets retrieval failed. Ensure that AWS credentials and SecretName are correct.")
# Replace with your weather API key and URL
#WEATHER_API_KEY = "5b9c4f40a61783899bdbaa014ededc29"
#WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather?q=Dhaka,uk&APPID=5b9c4f40a61783899bdbaa014ededc29"

@app.route('/api/weather')
def weather():
    hostname = socket.gethostname()
    current_datetime = datetime.now().strftime("%y%m%d%H%M")
    version = "1.0"  # Replace with your application version

    # Get weather data for London from the free weather API
    weather_data = get_weather_data("London")

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
