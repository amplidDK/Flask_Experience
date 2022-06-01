from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    page_title = 'Weather Forecast'
    forecast = weather_by_city('Moscow,Russia', 2)
    return render_template('index.html', page_title=page_title, forecast=forecast)


if __name__ == "__main__":
    app.run(debug=True)
