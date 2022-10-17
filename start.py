from concurrent.futures import process
from ctypes import resize
from email import message
from mimetypes import init
from select import select
import telebot
from telebot import types
import config 
import threading

bot = telebot.TeleBot(config.TOKEN)

us_num1=''
us_num2=''
us_proc = ''
us_resualt= None

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Привет, я личный секретарь Fedor Makarova! Есть идеи или неучет програмы, то пиши /supp. Так же есть другие команды можешь с ними ознокомиться: /help")

@bot.message_handler(commands=['help'])
def help(message):    
    bot.send_message(message.chat.id, "Я могу:\n /id - подробно расскажет про тебя,\n /supp - можешь обратиться к моему создателю")

@bot.message_handler(commands=['supp'])
def first_mes(message):
    markupKeyBoard1 = types.KeyboardButton(text = 'Поделиться идеей')
    markupKeyBoard2 = types.KeyboardButton(text = 'Рассказать о баге')
    markup = types.ReplyKeyboardMarkup(markupKeyBoard1,markupKeyBoard2 )
    msg = bot.send_message(message.chat.id, "Выбори что ты хочешь сделать: 1. Поделиться идеей 2. Рассказать о баге")
    bot.register_next_step_handler(msg, seconde_mes, markup)
def seconde_mes(message):
    #if message.text == 'Поделиться идеей':
    #if message.text ==  'Рассказать о баге':
    #   msg2 = bot
    msg = bot.send_message(message.chat.id, "Хорошо, опишите своё оброщение!")
    bot.register_next_step_handler(msg, last_mes)
def last_mes(message):
    bot.send_message(message.chat.id)
    (message.chat.861062442, "Оброщение пользователя" + message.username + " - " + message.text)

    bot.send_message(message.chat.id, "Спасибо за оброщение! Ожидайте ответа в бижайщем будущем!")

@bot.message_handler(commands=['id'])
def id(message):
    bot.send_message(message.chat.id, message.chat)

@bot.message_handler(commands=['culc'])
def hello_culc(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(message.chat.id,"Привет, привет! Начнём? Ввидите чесло:", reply_markup=markup)
    bot.register_next_step_handler(msg, first_step)
def first_step(message, us_resualt = None):
        global us_num1

        if us_resualt == None:
            us_num1 = str(message.text)
        else:
            us_num1 = str(us_resualt)
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        ib1 = types.KeyboardButten("+")
        ib2 = types.KeyboardButten("-")
        ib3 = types.KeyboardButten("*")
        ib4 = types.KeyboardButten(":")
        markup.add(ib1, ib2, ib3, ib4)

        msg = bot.send_message(message.chat.id,message.from_user.first_name + ", выберете действие:")
        bot.register_next_step_handler(msg, process_step)
#        bot.reply_to(message, "что-то пошло не так")

def process_step(message):
    try:
        global us_proc

        us_proc = message.text
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(message.chat.id, "ввидите действие", reply_markup=markup)
        bot.register_next_step_handler(msg, seconde_step)
    except Exception as e:
        bot.reply_to(message, "ой, ой что-то пошло не так")

def seconde_step(message):
    try:
        global us_num2

        us_num2 = int(message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        ib1 = types.KeyboardButten("продолжить", callback_data='butten1')
        ib2 = types.KeyboardButten("показать результат", callback_data='butten2') 
        markup.add(ib1 ,ib2)

        msg = bot.send_message(message.chat.id,"продолжить или показать результат?", reply_markup= markup)
        bot.register_next_step_handler(msg, alter_step)
    except Exception as e:
        bot.reply_to(message, "вот тут не ожидал неполадок")

def alter_step(message):
    try:
        calc()

        markup = types.ReplyKeyboardMarkup(selective=False)

        if message.text.lower() == 'показать результат':
            bot.send_message(message.chat.id, calcResultPrint(), reply_markup=markup)
        elif message.text.lower() == 'продолжить':
            first_step(message, us_resualt)
    except Exception as e: 
        bot.replay_to(message, "мдам проблемка с печенькой)")

def calcResultPrint():
    global us_num1, us_num2, us_proc, us_resualt

    return "Результат:" + str(us_num1) + " " + us_proc + " " + str(us_num2) + " = " + str(us_resualt)

def calc():
    global us_num1, us_num2, us_proc, us_resualt
    us_resualt = eval(str(us_num1)+ us_proc + str(us_num2) )
    return us_resualt

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

if __name__ == '__main__':
    t2 = threading.Thread(target=hello)
    t2.start()
bot.polling(none_stop=True)