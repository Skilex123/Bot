
import requests

appid = "763fdfa15aba6003346acaaa617a06b0"


def get_weather():
    s_city = 'Kiev'

    res = requests.get(
        url="http://api.openweathermap.org/data/2.5/weather",
        timeout= 10,
        params={
            'q': s_city,
            'type': 'like',
            'units': 'metric',
            'APPID': appid,
        },
    )
    try:
        data = res.json()
    except Exception as e:
        print("Exception (weather):", e)
    main_weather = data['main']
    return f"""
        місто: {s_city}
        температура: {main_weather["temp"]},
        відчувається як: {main_weather["feels_like"]},
        мінімальна: {main_weather["temp_min"]},
        максимальна: {main_weather["temp_max"]},
        тиск: {main_weather["pressure"]},
        видимість: {main_weather["humidity"]}
        """