from django.shortcuts import render
import requests


def get_weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3f582ab1cded33433680962f887f0e91'

    city = 'Tallinn'

    city_weather = requests.get(url.format(city)).json()

    temperature = (city_weather['main']['temp'] - 32) * 5 / 9

    weather = {
        'city': city,
        'temperature': round(temperature, 1),
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {'weather': weather}

    return context
