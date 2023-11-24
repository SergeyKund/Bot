import telebot
from telebot import types
import sqlite3
import re
# Initialize bot
bot = telebot.TeleBot("6477306765:AAHcaYpDomSiL4iIADJ4KcEZhcul2v3nAVo")
name = None
email = None


# Start command handler
@bot.message_handler(commands=['start'])
def cmd_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_order = types.KeyboardButton('Зробити замовлення')
    btn_consult = types.KeyboardButton('Консультація з продавцем')
    markup.row(btn_order, btn_consult)
    btn_social_media = types.KeyboardButton('Наші соціальні мережі')
    markup.row(btn_social_media)

    greeting_message = f'Доброго дня, {message.from_user.first_name}! Чим я можу вам допомогти?'
    bot.send_message(message.chat.id, greeting_message, reply_markup=markup)


# Handle "Консультація з продавцем"
@bot.message_handler(func=lambda message: message.text == 'Консультація з продавцем')
def process_consultation_command(message):
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton('Консультант Наталя', url='https://t.me/Nataliia3434')
    markup.add(item)

    bot.send_message(message.chat.id, "Наші консультанти:", reply_markup=markup)


# Обработчик команды "Зробити замовлення"
@bot.message_handler(func=lambda message: message.text == 'Зробити замовлення')
def process_order_command(message):
    conn = sqlite3.connect('myhouse.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), email TEXT NOT NULL, phone TEXT NOT NULL)')
    conn.commit()
    cur.close()

    # Запрашиваем имя пользователя
    bot.send_message(message.chat.id, "Введіть ваше ім'я")
    bot.register_next_step_handler(message, process_user_info)


def process_user_info(message):
    name = message.text.strip()

    # Запрашиваем email пользователя
    bot.send_message(message.chat.id, "Введіть ваш email")
    bot.register_next_step_handler(message, process_email, name)


def process_email(message, name):
    email = message.text.strip()

    # Запрашиваем номер телефона пользователя
    bot.send_message(message.chat.id, "Введіть ваш номер телефону")
    bot.register_next_step_handler(message, process_phone, name, email)


def process_phone(message, name, email):
    phone = message.text.strip()

    # Сохраняем информацию в базе данных
    conn = sqlite3.connect('C:/Users/Lenovo/Documents/GitHub/Bot/myhouse.sql')
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO users(name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
        conn.commit()
        bot.send_message(message.chat.id, "Добре")
        cur.close()
        conn.close()
    except Exception as e:
        bot.send_message(message.chat.id, f"При выполнении запроса произошла ошибка: {str(e)}")





bot.polling(none_stop=True)


