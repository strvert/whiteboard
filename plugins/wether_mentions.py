# coding: utf-8

from slackbot.bot import respond_to
from openweathermap import Openweather



@respond_to(r'天気|てんき|テンキ|weather')
def wether_mention(message):
    msg = message.body['text']


    weatherdata = weatherapi.getOnedayweather(date_str)
    for datum in weatherdata:
        reply_str += datum['time_str'] + "\t"
        reply_str += datum['japanese_main'] + "\n"

    message.reply(reply_str)
