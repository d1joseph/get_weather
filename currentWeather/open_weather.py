# request the weather from the openWeather API. Learn more https://openweathermap.org/api
# This project uses the Current Weather Data service.
# Current Weather Documentation - https://openweathermap.org/current
import requests as r
import json


# you'll need your own API key from openweather. Sign up is free.
# cp your key into the config file
with open('config.json') as f:
    config = json.load(f)


def get_weather(key=config['SECRET']):
    # Get to the current weather service endpoint and receive json object response
    city = str(input('Enter city: '))
    print('Getting weather for {}\n...\n'.format(city))
    
    try:
        url = r.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, key))
        data = url.json()
        
        for key, value in data.items():
            print(key,':', value)
    
    except r.exceptions.RequestException as e:
        raise SystemExit(e)


if __name__ == "__main__":
    get_weather()
