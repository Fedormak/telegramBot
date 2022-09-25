from email import message
import telebot
import config 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Привет! Во мне сидит колькулятор! Если хочешь можешь им воспользоваться)) Командой- /numb")

@bot.message_handler(commands=['numb'])
def first_numb(message):
    bot.send_message(message.chat.id, "Ну как ввиди первое чесло")

# @bot.message_handler(content_types=['text'])
#def repit(message):
#    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)