# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply


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
    message.reply('レポートは辛いですよね。頑張ってください。')


@respond_to(r'(?i)blackboard')
def bb_mention(message):
    message.reply('BlackBoard、とてもいいサービスですよね。使われれば。')


@default_reply()
def default_mention(message):
    message.reply('どうしましたか？まだそのメッセージにはうまくお返事できないようです……')
