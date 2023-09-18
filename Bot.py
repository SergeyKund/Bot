import webbrowser
import telebot
from telebot import types
from telebot import callback_data

bot = telebot.TeleBot('6477306765:AAHcaYpDomSiL4iIADJ4KcEZhcul2v3nAVo')


def message_start(message):
    bot.send_message(message.chat.id, f'Доброго дня {message.from_user.first_name}, чим я можу вам допомогти?')

@bot.message_handler(commands=['start'])
def button_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton('Зробити замовлення')
    btn_2 = types.KeyboardButton('Консультація з продавцем')
    markup.row(btn_1, btn_2)
    btn_3 = types.KeyboardButton('Подивитися каталог')
    btn_4 = types.KeyboardButton('Наші соціальні мережі')
    markup.row(btn_3, btn_4)
    bot.send_message(message.chat.id, f'Доброго дня {message.from_user.first_name}, чим я можу вам допомогти?', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text =='Консультація з продавцем')
def consultant(message):
    markup_consultant = types.InlineKeyboardMarkup()
    btn_consultant = types.InlineKeyboardButton('Консультант Наталя', url='https://t.me/Nataliia3434')
    markup_consultant.add(btn_consultant)
    bot.send_message(message.chat.id, 'Наші консультанти:', reply_markup=markup_consultant)
    btn_back = types.KeyboardButton('Назад')
    markup_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_back.row(btn_back)
    bot.send_message(message.chat.id, 'Виберіть опцію:', reply_markup=markup_back)




@bot.message_handler(func=lambda message: message.text == 'Наші соціальні мережі')
def social_media(message):
    markup_soc_media = types.InlineKeyboardMarkup()
    markup_soc_media.add(types.InlineKeyboardButton('Instagram', url='https://www.instagram.com/my.house.od/'))
    markup_soc_media.add(types.InlineKeyboardButton('Telegram-канал', url='https://t.me/myhouseod'))
    bot.send_message(message.chat.id, 'Наші соціальні мережі:', reply_markup=markup_soc_media)
    btn_back = types.KeyboardButton('Назад')
    markup_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_back.row(btn_back)
    bot.send_message(message.chat.id, 'Виберіть опцію:', reply_markup=markup_back)


@bot.message_handler(func=lambda message: message.text == 'Назад')
def back(message):
    button_start(message)



bot.polling(none_stop=True)