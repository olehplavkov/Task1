# If the user provides an invalid English word, return the custom response from get_info() and exit the function
    if word_info.__class__ is str:
        update.message.reply_text(word_info)
        return

    # get the word the user provided
    word = word_info['word']

    # get the origin of the word
    origin = word_info['origin']
    meanings = '\n'

    synonyms = ''
    definition = ''
    example = ''
    antonyms = ''

    # a word may have several meanings. We'll use this counter to track each of the meanings provided from the response
    meaning_counter = 1

    for word_meaning in word_info['meanings']:
        meanings += 'Meaning ' + str(meaning_counter) + ':\n'

        for word_definition in word_meaning['definitions']:
            # extract the each of the definitions of the word
            definition = word_definition['definition']

            # extract each example for the respective definition
            if 'example' in word_definition:
                example = word_definition['example']

            # extract the collection of synonyms for the word based on the definition
            for word_synonym in word_definition['synonyms']:
                synonyms += word_synonym + ', '

            # extract the antonyms of the word based on the definition
            for word_antonym in word_definition['antonyms']:
                antonyms += word_antonym + ', '

        meanings += 'Definition: ' + definition + '\n\n'
        meanings += 'Example: ' + example + '\n\n'
        meanings += 'Synonym: ' + synonyms + '\n\n'
        meanings += 'Antonym: ' + antonyms + '\n\n\n'

        meaning_counter += 1

    # format the data into a string
    message = f"Word: {word}\n\nOrigin: {origin}\n{meanings}"

    update.message.reply_text(message)

# run the start function when the user invokes the /start command 
dispatcher.add_handler(CommandHandler("start", start))

# invoke the get_word_info function when the user sends a message 
# that is not a command.
dispatcher.add_handler(MessageHandler(Filters.text, get_word_info))
updater.start_polling()
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
