from email import message
import telebot
import config 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Привет! Во мне сидит калькулятор! Если хочешь можешь им воспользоваться)) Командой- /culc")

@bot.message_handler(commands=['culc'])
def helloCulc(message):
    bot.send_message(message.chat.id,"ввидите первое чесло:")
    if (message.text == ):

def first_n(message):
    bot.send_message(message.chat.id,"какое будет действие?(+;-)")
    a = first_n.message
    bot.send_message(a)


# @bot.message_handler(content_types=['text'])
#def repit(message):
#    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)