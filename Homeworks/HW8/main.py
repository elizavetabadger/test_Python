import telebot
from config import TOKEN
import random
import urllib
bot = telebot.TeleBot(TOKEN)

def comrpes(messeg):
   str = messeg.text[0]
   bot.send_message(messeg.chat.id, str)
   bot.send_sticker(messeg.chat.id, 'CAACAgIAAxkBAAEG73Vjo1mRgC9-dIS5kUjjdMG09qeodAACXwEAAhAabSLLoLkqsC4-oywE')
   bot.send_message(messeg.chat.id, 'для повторного сжатия снова нажмите на кнопку "Сжать"')


"""Команда СТАРТ"""

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('Рандомное число')
    item2 = telebot.types.KeyboardButton('Кинуть кость')
    item3 = telebot.types.KeyboardButton('Как дела?')
    item4 = telebot.types.KeyboardButton('Сжать')
    item5 = telebot.types.KeyboardButton('Загадать число')
    item6 = telebot.types.KeyboardButton('Выбери знак зодиака')

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)


def random_number(message):
    bot.send_message(message.chat.id, str(random.randint(0, 2)))


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Привет, как дела?', parse_mode='html')
    elif message.text == 'Рандомное число':
        random_number(message)
    elif message.text == 'Как дела?':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1 = telebot.types.InlineKeyboardButton('Не очень', callback_data='1')
        item2 = telebot.types.InlineKeyboardButton('Хорошо', callback_data='2')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Отлично, а у вас?', reply_markup=markup)
    elif message.text == 'Кинуть кость':
        bot.send_message(message.chat.id, f'Вам выпало {(random.randint(1, 6))}')
    elif message.text == 'Сжать':
        mesg = bot.send_message(message.chat.id, 'Введите строку которую хотите сжать')
        bot.register_next_step_handler(mesg, comrpes)
    elif message.text == 'Загадать число':
        # есть кнопка задагай число. по нажатию бот загадывает чилсо. в ответ ты пытаешсья угадать чилсо. пишешь число,он сравнивается и пишет в итоге угадал или нет

        bot.send_message(message.chat.id, 'Угадай число')

        bot.register_next_step_handler(message, random_num)
    elif message.text == 'Выбери знак зодиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1 = telebot.types.InlineKeyboardButton('Овен', callback_data='5')
        item2 = telebot.types.InlineKeyboardButton('Телец', callback_data='6')
        item3 = telebot.types.InlineKeyboardButton('Близнецы', callback_data='7')
        item4 = telebot.types.InlineKeyboardButton('Рак', callback_data='8')
        item5 = telebot.types.InlineKeyboardButton('Лев', callback_data='9')
        item6 = telebot.types.InlineKeyboardButton('Дева', callback_data='10')
        item7 = telebot.types.InlineKeyboardButton('Весы', callback_data='11')
        item8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='12')
        item9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='13')
        item10 = telebot.types.InlineKeyboardButton('Козерог', callback_data='14')
        item11 = telebot.types.InlineKeyboardButton('Водолей', callback_data='15')
        item12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='16')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        bot.send_message(message.chat.id, 'Выбери свой знак', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Данный функционал находится в разработке')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG-fljpjGkXPzPkQ2JW8grQGVotdUNswACdAwAAtpcyEmJEqNPPIyvYiwE')

def random_num(mesg):
    number = str(random.randint(0,2))
    if mesg.text == number:
        bot.send_message(mesg.chat.id, 'Угадал')
    else: bot.send_message(mesg.chat.id, 'Попробуй снова')



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    n = int(call.data)   
    if n == 1:
        bot.send_message(call.message.chat.id, 'Почему?')
    elif n == 2:
        bot.send_message(call.message.chat.id, 'Я рад!')
    elif 5 <= n <= 16:
        check_zod = take_text(call.data)
        bot.send_message(call.message.chat.id, check_zod)
    

def take_text(call):
    nstr = int(call) - 5
    print(nstr)
    with open ('zodiac.txt', 'r', encoding='utf-8') as file:
        per_txt = file.read().splitlines()
        return per_txt[nstr]

@bot.message_handler(content_types=["sticker"])
def handle_docs_audio(message):
    # Получим ID Стикера
    sticker_id = message.sticker.file_id
    # Нужно получить путь, где лежит файл стикера на Сервере Телеграмма
    file_info = bot.get_file(sticker_id)
    # Теперь формируем ссылку и скачивам файл
    urllib.request.urlretrieve(f'http://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}', file_info.file_path)

bot.polling(none_stop=True)