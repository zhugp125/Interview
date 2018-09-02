#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# pip install requests
# pip install wxpy

# MacOS 10.13.4 验证过

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests

#bot = Bot()
# linux执行登录需要调用这句
bot = Bot(console_qr=2, cache_path='botoo.pkl')

def get_news():
    # 获取金山词霸每日一句，英文和翻译
    url = 'http://open.iciba.com/dsapi'
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note

def send_news():
    try:
        contens = get_news()
        # 你朋友的微信名称，不是备注，也不是微信账号
        my_friend = bot.friends().search(u'郁枫阁')[0]
        my_friend.send(contens[0])
        my_friend.send(contens[1])
        my_friend.send(u'快乐每一天')
        # 每天（86400秒）发送一次
        t = Timer(86400, send_news)
        t.start()
    except Exception as e:
        print(e)
        my_friend.send(u'今天消息发送失败了')

if __name__ == "__main__":
    send_news()