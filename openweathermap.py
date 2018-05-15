# coding: utf-8

import requests
import json
from datetime import datetime
import time
from openweather_token import API_TOKEN


class Openweather:

    def __init__(self):
        self.API_KEY = API_TOKEN
        self.api = "http://api.openweathermap.org/data/2.5/forecast?" \
                + "q={city_name},{country_code}&appid={api_key}&units=metric"
        self.city_name = "Tomakomai"
        self.country_code = "JP"
        self.japanese_wether = {'01d':"快晴", '02d':'晴れ', '03d':'くもり',
                '04d':'くもり', '09d':'小雨', '10d':'雨', '11d':'雷雨',
                '13d':'雪', '50d':'霧', '01n':"快晴", '02n':'晴れ',
                '03n':'くもり', '04n':'くもり', '09n':'小雨', '10n':'雨',
                '11n':'雷雨', '13n':'雪', '50n':'霧'}

    def requestweather(self):
        url = self.api.format(
                city_name = self.city_name, country_code = self.country_code,
                api_key = self.API_KEY
                )
        response = requests.get(url)
        weather_data = json.loads(response.text)
        return weather_data

    def getOnedayweather(self, request_date):
        weather_data = self.requestweather()
        oneday_weather_list = []
        for weathers in weather_data['list']:
            oneday_weather = weathers['weather'][0]
            weather_datetime = datetime.fromtimestamp(weathers['dt'])
            weather_date_str = "{0:02d}{1:02d}".format(
                    weather_datetime.month, weather_datetime.day
                    )
            md_str = "{0}月{1}日".format(
                    weather_datetime.month, weather_datetime.day,
                    weather_datetime.hour
                    )
            h_str = "{0}時".format(weather_datetime.hour)
            if weather_date_str == request_date:
                oneday_weather['date_str'] = md_str
                oneday_weather['time_str'] = h_str
                oneday_weather['japanese_main'] = self.japanese_wether[
                       oneday_weather['icon']
                       ]
                oneday_weather_list.append(oneday_weather)

        return oneday_weather_list

    def getCityname(self):
        return self.city_name
