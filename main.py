import telebot
from telebot import  types

token = '7499780211:AAGYyIfyh0ANcuQoofZMCZvociYCEcw8roI'
bot = telebot.TeleBot(token)


# --- BOT MESSAGE --------------------------------------------


@bot.message_handler(commands=['tato', 'mama', 'start', 'stop', 'b'])
def bot_commands(message):
    mes = ''
    if message. text == '/tato':
        mes = 'tata nema doma'
    elif message.text == '/mama':
        mes = 'mamu nema doma'
    elif message.text == '/start':
        mes = 'програму запущено щоб зупинит її напишіть /stop'
    elif message.text == '/stop':
        mes = 'програму зупинено'
    elif message.text == '/b':
        bot_buttons(message)
        return True

    bot.send_message(message.chat.id, mes)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    mes = message.text + ' - Це просто текст'
    bot.send_message(message.chat.id, mes)


# ---ФУНКЦІЇ---------------------------------------------------------


def bot_buttons(message):
    keyboard = types. ReplyKeyboardMarkup(one_time_keyboard=True)

    button_1 = types.KeyboardButton(text='кнопка1')
    button_2 = types.KeyboardButton(text='кнопка2')
    button_3 = types.KeyboardButton(text='кнопка3')
    button_4 = types.KeyboardButton(text='кнопка4')

    keyboard.add (button_1, button_2, button_3, button_4)

    msg = bot.send_message(message.chat.id, message.text, reply_markup=keyboard)
    bot.register_next_step_handler(msg, button_if)


def button_if (message):
    if message.text == 'кнопка1':
        bot.send_message(message.chat.id, '1.Закопати путіна')
    elif message.text == 'кнопка2':
        bot.send_message(message.chat.id, '1.Закопати шойгу')
    else:
        bot.send_message(message.chat.id, '3,4.Запуск ')



if __name__ ==  '__main__':
    bot.polling()
