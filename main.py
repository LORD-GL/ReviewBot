# -*- coding: utf-8 -*-
"""
    -------------------
    | Maded by LeLord |
    -------------------
    ver. 12.04.2021 (MM.DD.YYYY)
    https://t.me/LORD_GL 
"""
import telebot

HTTP_API = ""

bot = telebot.Telebot(HTTP_API)

def handlers():
    @bot.message_handler(command=['start'])
    def start(message):
        IntroText = """
        Hi, welcome to the students goverment!
        Leave your review:
        """
        bot.send_message(message.chat.id, IntroText)

    @bot.message_handler(content_types=["text"])
    def writeRev(message):
        file = open('data.txt', 'a')
        file.write(f"\n-----\nName: {message.from_user} \nid: {message.chat.id} \ndate: {message.date}\n----\n")
        file.close()