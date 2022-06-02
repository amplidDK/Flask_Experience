import requests
import setting


def weather_by_city(city, period):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    payload = {
        'key': setting.API_KEY,
        'q': city,
        'format': 'json',
        'num_of_days': period,
        'lang': 'ru'
    }
    try:
        response = requests.get(weather_url, params=payload)
        response.raise_for_status()
        result = response.json()
        if 'data' in result:
            if 'current_condition' in result['data']:
                try:
                    return result['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except (requests.RequestException, ValueError) as error:
        print(f"Error has accured: {error}")
