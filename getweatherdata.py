import urllib.request
import requests
from dotenv import load_dotenv
import json
import os


class GetWeatherData:
    def __init__(self, lang):
        # get apikey
        load_dotenv()
        self.apiKey = os.environ.get("apikey")
    
    
        # get location
        with urllib.request.urlopen("https://geolocation-db.com/json") as url:
            data = json.loads(url.read().decode())
        self.city = data["city"]    
    
        # language
        self.lang: str = lang


    """
    Get weather data from openweathermap
    """
    def get_weather_info(self):
        # get weather data from openweathermap's api
        api = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.apiKey}&lang={self.lang}&units=metric"
        result = requests.get(api)
        result = json.loads(result.text)
        # [weather information, weather icon, temperature informatino]
        return [result["weather"][0]["icon"], result["weather"][0]["description"].upper(), result["main"]] 


if __name__ == "__main__":
    gwd = GetWeatherData()
    gwd.get_weather_info()
