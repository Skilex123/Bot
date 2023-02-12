import telebot
from telebot import types

from wheather import get_weather

token = "5698439744:AAFy1xbG_WMFGn-TgAM_BGr6dJ_l4sZcpx4"

bot = telebot.TeleBot(token)

map_url = 'https://www.google.com.ua/maps/place/Mahazyn+Kvitiv+%22Nimfeya%22/@50.2816994,28.6087086,17.87z/data=!4m5!3m4!1s0x0:0x5e89e29b879186cc!8m2!3d50.2812976!4d28.6087867?hl=ru'


def get_change_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    start_service = types.InlineKeyboardButton(text='Локация', callback_data='location')
    start_system = types.InlineKeyboardButton(text='Погода', callback_data='wheather')
    markup.add(start_service, start_system)
    return markup


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        'Выберите что вам нужно',
        reply_markup=get_greetings_keyboard(),
    )


@bot.callback_query_handler(func=lambda call: call.data == 'location')
def location_callback(call):
    bot.send_message(call.message.chat.id, map_url)


@bot.callback_query_handler(func=lambda call: call.data == 'wheather')
def weather_callback(call):
    bot.send_message(call.message.chat.id, get_weather())


def get_greetings_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Меню")
    markup.add(item1)
    return markup


@bot.message_handler(func=lambda message: message.text == 'Меню')
def reply_button_menu(message):
    return bot.send_message(message.chat.id, 'Меню', reply_markup=get_change_keyboard())


if __name__ == '__main__':
    bot.infinity_polling()

