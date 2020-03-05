from telebot import types


def set_main_menu_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.row(types.InlineKeyboardButton(text='New MEME',
                                            callback_data='new_meme'))
    keyboard.row(types.InlineKeyboardButton(text='About us',
                                            callback_data='about'))

    return keyboard
