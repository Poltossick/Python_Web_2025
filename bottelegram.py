token = '8066468637:AAHSvpRy6QAlpOO8npEUwjXH0Abi15OwJL8'

import telebot
from telebot import types

bot = telebot.TeleBot(token)

kb = types.ReplyKeyboardMarkup(row_width=2)
btn1 = types.KeyboardButton('/link')
btn2 = types.KeyboardButton('/help')
btn3 = types.KeyboardButton('how are you?')
kb.add(btn1, btn2, btn3)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Я запущен и буду повторять за Вами',
                     reply_markup=kb)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                     'Я пока ничего не умею, я просто ваше эхо')

@bot.message_handler(content_types=['text'])
def parrot(message):
    if message.text.strip().lower() == 'привет':
        bot.send_message(message.chat.id, 'Ну, привет!')
    elif message.text.strip().lower() == 'how are you?':
        # bot.send_message(message.chat.id, '👍')
        answer = types.InlineKeyboardMarkup(row_width=2)
        btn_good = types.InlineKeyboardButton('Хорошо', callback_data='good')
        btn_bad = types.InlineKeyboardButton('Плохо', callback_data='bad')
        answer.add(btn_good, btn_bad)
        bot.send_message(message.chat.id, 'У меня то хорошо, а у тебя?',
                         reply_markup=answer)
    else:
        bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['link'])
def url_message(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Сайт Яндекс', link='https://ya.ru')
    markup.add(btn)
    bot.send_message(message.chat.id, 'Перейти на сайт Яндекса',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'good':
        bot.send_message(call.message.chat.id, 'ну и флаг в руки')
    if call.data == 'bad':
        bot.send_message(call.message.chat.id, 'да и черт с ним')

bot.infinity_polling(none_stop=True)
