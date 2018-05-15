# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random


@respond_to('あいうえお')
def aiueo_mention(message):
    message.reply('かきくけこ')


@respond_to('頑張って|がんばって')
def fight_mention(message):
    message.reply('ありがとうございます。')


@listen_to('¯\\_(ツ)_/¯')
def tugao_mention(message):
    message.reply('¯\\_(ツ)_/¯')


@respond_to('ありがとう')
def thanks_mention(message):
    message.reply('お役に立てたようで幸いです。どういたしまして。')


@respond_to(r'^ping\s+\d+\.\d+\.\d+\.\d+\s*$')
def ping_mention(message):
    message.reply('pingコマンドですか？Slackでは実行できませんよ？？')


@respond_to('レポート|れぽーと')
def report_mention(message):
    rnd_num = random.randint(0,2)
    if rnd_num == 0:
        message.reply('レポートは辛いですよね。頑張ってください。')
    elif rnd_num == 1:
        message.reply('前日の夜にやるようなことにならないよう頑張りましょうね。')
    elif rnd_num == 2:
        message.reply('とりあえず提出に間に合うように書き進めるんですよ！！')


@respond_to(r'(?i)blackboard')
def bb_mention(message):
    message.reply('BlackBoard、とてもいいサービスですよね。使われれば。')


@default_reply()
def default_mention(message):
    message.reply('どうしましたか？まだそのメッセージにはうまくお返事できないようです……')
