# request the weather from the openWeather API. Learn more https://openweathermap.org/api
# This project uses the Current Weather Data service.
# Current Weather Documentation - https://openweathermap.org/current
import requests as r
import json

# My API key
key = 'f09a88a1c65a34bdf1c018fd54cc876e'
city = str(input('Enter a city: ')).lower()


def get_weather(city, API_KEY=key):

    # Get Current Weather service endpoint and output to json
    url = r.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, API_KEY))
    data = url.json()


    for key, value in data.items():
        print(key,':', value)



if __name__ == "__main__":
    get_weather(city)
