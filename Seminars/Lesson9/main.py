# import telebot
# from config import TOKEN
# import random
# bot = telebot.TeleBot(TOKEN)


# """Команда СТАРТ"""


# @bot.message_handler(commands=['start'])
# def welcome(message):
#     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

#     item1 = telebot.types.KeyboardButton('Рандомное число')
#     item2 = telebot.types.KeyboardButton('Кинуть кость')

#     markup.add(item1, item2)

#     bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)


# def random_number(message):
#     bot.send_message(message.chat.id, str(random.randint(1, 10)))

# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text == 'привет':
#         bot.send_message(message.chat.id, 'Привет, как дела?')
#     elif message.text == 'Рандомное число':
#         random_number(message)
#     elif message.text == 'Кинуть кость':
#         bot.send_message(message.chat.id, f'Вам выпало {(random.randint(1, 6))}')
#     else:
#         bot.send_message(message.chat.id, 'Данный функционал находится в разработке')


# bot.polling(none_stop=True)

import telebot
import random
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

anecdoteList = ['Когда ты умер, ты об этом не знаешь, только тяжело твоим близким. То же самое, когда ты тупой... anekdotov.net',
                '— Продайте мне собаку. — Суку? — Не, с@ку не надо, давайте нормальную. — Сука — это пол собаки. — А зачем мне пол собаки? Давайте целую. anekdotov.net',
                'Если исключить из моего меню те продукты, которые не рекомендуют гастроэнтеролог, кардиолог, невролог, эндокринолог и уролог, то питаться мне можно только водой, и то — кипяченой. anekdotov.net',
                'Психиатр поздравляет своего пациента с прогрессом в лечении. — И это вы называете прогрессом??? Шесть месяцев назад я был Наполеоном, а сейчас — никто... anekdotov.net',
                'У вождя племени людоедов берут интервью. Журналисты задают массу вопросов. Вождь охотно отвечает, рассказывает... — Ну, а теперь последний вопрос: скажите, как Вы относитесь к евреям? — Вы знаете, я считаю антисемитизм глупейшим предрассудком. Евреи абсолютно такие же люди, как и все другие! Я и племени своему это постоянно объясняю. Но не едят! anekdotov.net']

"""Команда СТАРТ"""
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('У меня плохое настроение')
    item2 = telebot.types.KeyboardButton('У меня хорошее настроение')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Дарова', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def sendText(message):
    if message.text == 'У меня плохое настроение':
        bot.send_message(message.chat.id, str(random.choice(anecdoteList)))
    elif message.text == 'У меня хорошее настроение':
        bot.send_message(message.chat.id, 'Всю жизнь тебе писать на питоне!')
    else:
        bot.send_message(message.chat.id, '123')


bot.polling(none_stop=True)