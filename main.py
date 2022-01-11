# -*- coding: utf-8 -*-
"""
    -------------------
    | Maded by LeLord |
    -------------------
    ver. 12.04.2021 (MM.DD.YYYY)
    https://t.me/LORD_GL 
"""
import telebot

HTTP_API = "5056002443:AAHDdOkl2s0xPSrAKL0Hj85BkbMsdpNd1yQ"

bot = telebot.TeleBot(HTTP_API)

@bot.message_handler(commands=["start"])
def start(message):
    IntroText = """
Hi, welcome to the students government!
Leave your review:
    """
    bot.send_message(message.chat.id, IntroText)

@bot.message_handler(content_types=["text"])
def writeRev(message):
    file = open('data.txt', 'a')
    file.write(f"Name: {message.chat.username}\n")
    file.write(f"id: {message.chat.id}\n")
    file.write(f"date: {message.text}\n----\n")
    file.close()

bot.polling(none_stop=True, interval=0)