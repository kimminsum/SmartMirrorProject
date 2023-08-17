from flask import Flask, render_template, jsonify
from getweatherdata import GetWeatherData
import datetime


app = Flask(__name__)


def update_clockinfo():
    while True:
        d = datetime.datetime.now()
        date = f"{d.year}.{d.month}.{d.day}"
        times = f"{d.hour}:{d.minute}:{d.second}"
        yield dict(date=date, times=times)


def update_wttrinfo():
    while True:
        forecast_icon, forecast, temperature = GetWeatherData("en").get_weather_info()
        forecast_icon = f"https://openweathermap.org/img/wn/{forecast_icon}.png"
        yield dict(forecast_icon=forecast_icon, forecast=forecast, temperature=temperature)
"""
Main Page
"""
@app.route('/')
def home():
    return render_template("home.html")
"""
Update clock
"""
@app.get("/clock")
def clock():
    return jsonify(next(tick))
"""
Update wttrinfo
"""
@app.get("/wttrinfo")
def wttrinfo():
    return jsonify(next(DB))


if __name__ == "__main__":
    tick = update_clockinfo()
    DB = update_wttrinfo()
    app.run()

