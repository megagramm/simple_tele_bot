import telebot
import requests
import bs4
import time
import sqlite3
import re

token = "5612180908:AAGYgFaGNaEn2u0V0NcJx-FTSHySgeceJTg"
# CHANNEL_NAME = "@fpy_69"
CHANNEL_NAME = "@megarammTestBotChannal"

bot = telebot.TeleBot(token)
conn = sqlite3.connect('megagrammBot.sqlite')
cursor = conn.cursor()

try:
    cursor.execute('''CREATE TABLE IF NOT EXIST news(text longtext,short_text varchar(300), date datetime)''')
except:
    pass

#bot.send_message(CHANNEL_NAME, 'Тестовое сообщение от бота')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Тестовое</b> сообщение бота', parse_mode='html')
@bot.message_handler(commands=['end'])
def end(message):
    bot.send_message(message.chat.id, '<b>Конец сообщения</b>', parse_mode='html')

help(telebot)
bot.polling(none_stop=True)