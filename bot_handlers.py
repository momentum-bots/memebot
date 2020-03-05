import telebot
import config
import keyboards


bot = telebot.TeleBot(config.BOT_TOKEN)
print(bot.get_me())


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     'Main menu',
                     reply_markup=keyboards.set_main_menu_keyboard())


@bot.message_handler(content_types=['text'])
def text_handler(message):
    bot.send_message(message.chat.id, message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'about':
        bot.send_message(call.message.chat.id, 'We are meme creators!')
        bot.answer_callback_query(call.id, '')


bot.polling(none_stop=True)
