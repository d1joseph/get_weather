# request the weather from the openWeather API. Learn more https://openweathermap.org/api
# This project uses the Current Weather Data service.
# Current Weather Documentation - https://openweathermap.org/current
import requests as r

# API key - you'll need your own API key from openweather. Sign up is free.
key = 'your key'
city = str(input('Enter a city: ')).lower()


def get_weather(city, API_KEY=key):

    # Get Current Weather service endpoint and output to json
    url = r.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, API_KEY))
    data = url.json()


    for key, value in data.items():
        print(key,':', value)



if __name__ == "__main__":
    get_weather(city)
