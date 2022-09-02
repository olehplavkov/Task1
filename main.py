from email import message
from tkinter import PhotoImage
from turtle import rt
import telebot
from telebot import types
language = ukrainian

bot = telebot.TeleBot('5444617281:AAFqUQptRNXdsRrwSgumYS38m9toSDDnJFQ')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привіт, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
      bot.send_message(message.chat.id, "І тобі привіт", parse_mode='html')
    
    elif message.text == "id":
        bot.send_message(
            message.chat.id, f"Твій ID: {message.from_user.id}", parse_mode='html')
    
    elif message.text == "send photo":
        photo=open('9.png', 'rb')
        bot.send_photo(update.message.chat_id, photo)

    else:
        bot.send_message(message.chat.id, "Я тебе не розумію", parse_mode='html')



@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, я в захваті від картинки')

@bot.message_handler(commands=['website'])
def website(message):
    markup =  types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Відвідати веб-сайт", url="https://toloka.to")) 
    bot.send_message(message.chat.id, 'Перейдіть на сайт', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup =  types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Веб-сайт')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейдіть на сайт', reply_markup=markup)


bot.polling (none_stop = True)
