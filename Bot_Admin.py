import telebot
import sqlite3

# Инициализация второго бота
second_bot = telebot.TeleBot("6690483976:AAFaiW9fZg0ri6RROXyvvtnXH0Mo0nMqHs0")

# Обработчик команды /get_info
@second_bot.message_handler(commands=['get_info'])
def get_info(message):
    # Подключение к базе данных
    conn = sqlite3.connect('C:/Users/Lenovo/Documents/GitHub/Bot/myhouse.sql')
    cur = conn.cursor()

    # Выборка информации из базы данных
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()

    # Отправка информации в чат второго бота
    for row in rows:
        name, email, phone = row[1], row[2], row[3]
        second_bot.send_message(message.chat.id, f"Информация из базы данных:\nИмя: {name}\nEmail: {email}\nТелефон: {phone}")

    # Закрытие соединения
    conn.close()

# Запуск второго бота
second_bot.polling(none_stop=True)

