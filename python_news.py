import requests
from bs4 import BeautifulSoup


def get_html_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except(requests.RequestException, ValueError):
        return False


def get_python_news():
    page = get_html_page('https://tproger.ru/tag/python/')
    if page:
        soup = BeautifulSoup(page, 'html.parser')
        all_news = soup.findAll('h2', class_="article__title article__title--icon")
        news_list = []
        for index in all_news:
            title = index.find('a').text
            link = index.find('a')['href']
            news_list.append({
                'title': title,
                'link': link
            })
        return news_list
    return False
