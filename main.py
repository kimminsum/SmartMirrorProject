from flask import Flask, render_template

from getweatherdata import GetWeatherData


app = Flask(__name__)

@app.route('/')
def home():
    forecast_icon, forecast, temperature = GetWeatherData("en").get_weather_info()
    return render_template("home.html", forecast_icon=forecast_icon, forecast=forecast, temperature=temperature)

# @app.route("/get_wttrinfo")
# def get_wttrinfo():


if __name__ == "__main__":
    app.run()

