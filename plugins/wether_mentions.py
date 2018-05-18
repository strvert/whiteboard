# coding: utf-8

from slackbot.bot import respond_to
from openweathermap import Openweather
from datetime import datetime
from datetime import date
from word_to_date import WordToDate

api = Openweather()
to_date = WordToDate()

@respond_to(r'天気|てんき|テンキ|weather')
def wether_mention(message):
    msg = message.body['text']
    weather = api.getOnedayWeather(to_date.wordToDate(msg))
    if len(weather) is not 0:
        reply_str = '{0} {1}の天気をお伝えします。\n'.format(weather[0]['date_str'], api.getCityname())
        for datum in weather:
            reply_str += datum['time_str'] + "\t"
            reply_str += datum['japanese_main'] + "\n"

        message.reply(reply_str)
    else:
        message.reply("{0}月{1}日の天気情報を取得できませんでした。（取得範囲は５日後までとなっています。）".format(
            to_date.wordToDate(msg).month, to_date.wordToDate(msg).day
        ))
