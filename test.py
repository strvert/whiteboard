from openweathermap import Openweather
from datetime import date
from word_to_date import WordToDate

test = Openweather()
to_date = WordToDate()

print(to_date.wordToDate("あしたのてんき"))
print(to_date.findDaywords("あしたのてんき"))

weather = test.getOnedayWeather(date.today())
print(weather)