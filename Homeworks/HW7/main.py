import telebot
import random
from config import token

bot = telebot.TeleBot(token)

anecdoteList = ['Когда ты умер, ты об этом не знаешь, только тяжело твоим близким. То же самое, когда ты тупой... anekdotov.net',
                '— Продайте мне собаку. — Суку? — Не, с@ку не надо, давайте нормальную. — Сука — это пол собаки. — А зачем мне пол собаки? Давайте целую. anekdotov.net',
                'Если исключить из моего меню те продукты, которые не рекомендуют гастроэнтеролог, кардиолог, невролог, эндокринолог и уролог, то питаться мне можно только водой, и то — кипяченой. anekdotov.net',
                'Психиатр поздравляет своего пациента с прогрессом в лечении. — И это вы называете прогрессом??? Шесть месяцев назад я был Наполеоном, а сейчас — никто... anekdotov.net',
                'У вождя племени людоедов берут интервью. Журналисты задают массу вопросов. Вождь охотно отвечает, рассказывает... — Ну, а теперь последний вопрос: скажите, как Вы относитесь к евреям? — Вы знаете, я считаю антисемитизм глупейшим предрассудком. Евреи абсолютно такие же люди, как и все другие! Я и племени своему это постоянно объясняю. Но не едят! anekdotov.net']

"""Команда START"""
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('У меня плохое настроение')
    item2 = telebot.types.KeyboardButton('У меня хорошее настроение')
    item3 = telebot.types.KeyboardButton('Калькулятор')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Добро пожаловать!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def sendText(message):

    example: str = message.text

    if message.text == 'У меня плохое настроение':
        bot.send_message(message.chat.id, str(random.choice(anecdoteList)))
    elif message.text == 'У меня хорошее настроение':
        bot.send_message(message.chat.id, 'Всю жизнь тебе писать на питоне!')
    elif message.text == 'Калькулятор':
        bot.send_message(message.chat.id, 'Введите числа в виде a+b')
    elif example.__contains__('*'):
        result = parseExample('*', example)
        bot.send_message(message.chat.id, f'Вот результат = {result}')
    elif example.__contains__('+'):
        result = parseExample('+', example)
        bot.send_message(message.chat.id, f'Вот результат = {result}')
    elif example.__contains__('-'):
        result = parseExample('-', example)
        print(result)
        bot.send_message(message.chat.id, f'Вот результат = {result}')
    elif example.__contains__('/'):
        result = parseExample('/', example)
        bot.send_message(message.chat.id, f'Вот результат = {result}')
    else:
        bot.send_message(message.chat.id, 'Ошибка')

def parseExample(symbol, example):
    firstNumber = example.split(symbol)[0]
    secondNumber = example.split(symbol)[1]
    return getResult(symbol, int(firstNumber), int(secondNumber))

def getResult(symbol, a, b):
    if symbol == '+':
        return summ(a, b)
    elif symbol == '-':
        return diff(a, b)
    elif symbol == '*':
        return mult(a, b)
    elif symbol == '/':
        return div(a, b)

def summ(a, b):
    return a + b

def diff(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

bot.polling(none_stop=True)