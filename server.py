from flask import Flask, render_template
from weather import weather_by_city
from python_news import get_python_news

app = Flask(__name__)


@app.route('/')
def index():
    page_title = 'Шлакоблокунь Москвы'
    forecast = weather_by_city('Moscow,Russia', 2)
    news_list = get_python_news()
    return render_template('index.html', page_title=page_title, forecast=forecast, news_list=news_list)


if __name__ == "__main__":
    app.run(debug=True)
