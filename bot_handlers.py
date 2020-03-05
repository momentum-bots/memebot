import telebot
import config


bot = telebot.TeleBot(config.BOT_TOKEN)
print(bot.get_me())


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Main menu')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    bot.send_message(message.chat.id, message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    pass


bot.polling(none_stop=True)
