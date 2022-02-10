# -*- coding: utf-8 -*-
"""
    -------------------
    | Maded by LeLord |
    -------------------
    ver. 12.04.2021 (MM.DD.YYYY)
    https://t.me/LORD_GL 
"""
import telebot, datetime

HTTP_API = "5056002443:AAHDdOkl2s0xPSrAKL0Hj85BkbMsdpNd1yQ"

bot = telebot.TeleBot(HTTP_API)

REV_BUTTON_TEXT = "New Review"
rev_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
rev_keyboard.row(REV_BUTTON_TEXT)

@bot.message_handler(commands=["start"])
def start(message):
    IntroText = """
Hi, welcome to the students government!
Leave your review:
    """
    bot.send_message(message.chat.id, IntroText)

@bot.message_handler(func = lambda message: message.text == REV_BUTTON_TEXT)
def new_rev(message):
    bot.send_message(message.chat.id, "Send new review:")

@bot.message_handler(content_types=["text"])
def writeRev(message):
    try:
        file = open('data.txt', 'a')
        file.write(f"Name: {message.chat.username}\n")
        file.write(f"id: {message.chat.id}\n")
        file.write(f"Text: {message.text}\n")
        file.write(f"Date: {datetime.datetime.now()}\n----\n")
        file.close()
        bot.send_message(message.chat.id, "Thank for your review!\n", reply_markup = rev_keyboard)
    except:
        bot.send_message(message.chat.id, "Something went wrong!", reply_markup = rev_keyboard)


bot.polling(none_stop=True, interval=0)