# coding: utf-8

import re
from datetime import date
from datetime import timedelta
import mojimoji


class WordToDate:

    def __init__(self):
        self.today_words = '今日|きょう|today'
        self.tomorrow_words = '明日|翌日|あした|アシタ|あす|tomorrow'
        self.in_two_days_words = '明後日|あさって'
        self.in_three_days_words = '明々後日|しあさって'
        self.day_words = '{0}|{1}|{2}|{3}'.format(
            self.today_words, self.tomorrow_words, self.in_two_days_words, self.in_three_days_words)
        self.today_date = date.today()
        self.tomorrow_date = date.today() + timedelta(days=1)
        self.in_two_days_date = date.today() + timedelta(days=2)
        self.in_three_days_date = date.today() + timedelta(days=3)

    def getDayWords(self):
        return self.day_words

    def getTodayWords(self):
        return self.today_words

    def getTomorrowWords(self):
        return self.tomorrow_words

    def getInTwoDaysWords(self):
        return self.in_two_days_words

    def getInThreeDaysWords(self):
        return self.in_three_days_words

    def findDaywords(self, msg):
        return re.findall(self.day_words, msg)[0]

    def wordToDate(self, day_word):
        if re.search('(?:[0-9]|[０-９]){1,2}月(?:[0-9]|[０-９]){1,2}日', day_word):
            day_word_list = re.findall('((?:[0-9]|[０-９]){1,2})月((?:[0-9]|[０-９]){1,2})日', day_word)[0]
            try:
                return date(date.today().year,
                            int(mojimoji.zen_to_han(day_word_list[0])), int(mojimoji.zen_to_han(day_word_list[1])))
            except:
                return None

        elif re.search('(?:[0-9]|[０-９]){1,2}[/／](?:[0-9]|[０-９]){1,2}', day_word):
            day_word_list = re.findall('((?:[0-9]|[０-９]){1,2})[/／]((?:[0-9]|[０-９]){1,2})', day_word)[0]
            try:
                return date(date.today().year,
                            int(mojimoji.zen_to_han(day_word_list[0])), int(mojimoji.zen_to_han(day_word_list[1])))
            except:
                return None

        elif re.search('(?:[0-9]|[０-９])+日後', day_word):
            day_word_list = re.findall('((?:[0-9]|[０-９])+)日後', day_word)
            try:
                return self.today_date + timedelta(days=int(day_word_list[0]))
            except:
                return None

        elif re.search('(?:[0-9]|[０-９])+日前', day_word):
            day_word_list = re.findall('((?:[0-9]|[０-９])+)日前', day_word)
            try:
                return self.today_date - timedelta(days=int(day_word_list[0]))
            except:
                return None

        elif re.search(self.day_words, day_word):
            if re.search(self.in_three_days_words, day_word):
                return self.in_three_days_date
            elif re.search(self.in_two_days_words, day_word):
                return self.in_two_days_date
            elif re.search(self.tomorrow_words, day_word):
                return self.tomorrow_date
            elif re.search(self.today_words, day_word):
                return self.today_date
        else:
            return None
