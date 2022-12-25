import telebot
import random
from config import TOKEN

token = '5846390360:AAHFUXe2vXi2ZYJw4S71uFe0DcU0YHq5aIo'

bot = telebot.TeleBot(TOKEN)

def comrpes(messeg):
    str = Compres.Compress(messeg.text)
    bot.send_message(messeg.chat.id, str)
    bot.send_sticker(messeg.chat.id, 'CAACAgIAAxkBAAEG73Vjo1mRgC9-dIS5kUjjdMG09qeodAACXwEAAhAabSLLoLkqsC4-oywE')
    bot.send_message(messeg.chat.id, 'для повторного сжатия снова нажмите на кнопку "Сжать"')