# coding: utf-8

print("SlackのAPI Tokenを入力してください")
SLACK_API_TOKEN = input()

with open('slackbot_settings.py', 'w') as f:
    f.write("PLUGINS = ['plugins']\n")
    f.write("API_TOKEN = '" + SLACK_API_TOKEN + "'\n")

print("OpenWeatherMapのAPP Tokenを入力してください")
WEATHER_APP_TOKEN = input()

with open('openweather_token.py', 'w') as f:
    f.write("API_TOKEN = '" + WEATHER_APP_TOKEN + "'\n")
