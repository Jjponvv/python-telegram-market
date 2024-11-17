import telebot
import makebot as data

bot = telebot.TeleBot(data.API)


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.username == data.ADMIN:
        bot.send_message(message.chat.id, "hello admin")
    else:
        bot.send_message(message.chat.id, "hello user")

bot.polling(non_stop=True)
