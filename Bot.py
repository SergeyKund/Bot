import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types.web_app_info import WebAppInfo


# Initialize bot and dispatcher
bot = Bot(token="6477306765:AAHcaYpDomSiL4iIADJ4KcEZhcul2v3nAVo")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())


# Start command handler
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_order = types.KeyboardButton('Зробити замовлення')
    button_consult = types.KeyboardButton('Консультація з продавцем')
    keyboard.row(button_order, button_consult)
    button_social_media = types.KeyboardButton('Наші соціальні мережі')
    keyboard.row(button_social_media)

    greeting_message = f'Доброго дня, {message.from_user.first_name}! Чим я можу вам допомогти?'
    await message.answer(greeting_message, reply_markup=keyboard)


# Handle "Консультація з продавцем"
@dp.message_handler(lambda message: message.text == 'Консультація з продавцем')
async def process_consultation_command(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton('Консультант Наталя', url='https://t.me/Nataliia3434')
    markup.add(item)

    await message.reply("Наші консультанти:", reply_markup=markup)


# Handle "Зробити замовлення"
@dp.message_handler(lambda message: message.text == 'Зробити замовлення')
async def process_order_command(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton('Відкрити форму', web_app=WebAppInfo(url='https://www.instagram.com/my.house.od/'))
    markup.add(item)

    await message.reply("Заповніть нашу форму:", reply_markup=markup)


# Handle "Наші соціальні мережі"
@dp.message_handler(lambda message: message.text == 'Наші соціальні мережі')
async def social_media(message: types.Message):
    markup_soc_media = types.InlineKeyboardMarkup()
    markup_soc_media.add(types.InlineKeyboardButton('Instagram', url='https://www.instagram.com/my.house.od/'))
    markup_soc_media.add(types.InlineKeyboardButton('Telegram-канал', url='https://t.me/myhouseod'))

    await message.answer('Наші соціальні мережі:', reply_markup=markup_soc_media)




if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)