import urllib.request
import requests
import json


from dotenv import load_dotenv
import os


def main():
    # get location
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
    city = data["city"]

    # get apikey
    load_dotenv()
    apiKey = os.environ.get("apikey")
    # language
    lang = "en"
    # change fahrenheit to celsius
    units = "metric"
    # get weather data from openweathermap's api
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"
    result = requests.get(api)
    result = json.loads(result.text)
    print(result)


if __name__ == "__main__":
    main()

