from telegram.ext import Updater
from telegram.ext import CommandHandler
import datetime


TOKEN = "5191680095:AAGajm-rTiZBt6T32R9mBKuzAZXZeolzYzw"

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

def txt_write(id, text):
    tex = ' '.join(text)
    now =datetime.datetime.now()
    now = now.strftime('%d-%m-%Y %H:%M:%S')
    date = str(id) + ';' + now + ';' + tex
    with open('datefile.txt', 'a', encoding='utf-8') as fin:
        fin.write(date + '\n')

def start(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привет! Это Бот калькулятор.")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="вызовите каманду /kal (и через пробел ведите пример. Например: /kal 5 * 3)")
    a = update.effective_chat.id
    print(a)

start_handler = CommandHandler('start', start)


def kal(update, context):

    if context.args:

        if context.args[1] == '+':
            pes = int(context.args[0]) + int(context.args[2])
        if context.args[1] == '-':
            pes = int(context.args[0]) - int(context.args[2])
        if context.args[1] == '*':
            pes = int(context.args[0]) * int(context.args[2])
        if context.args[1] == '/':
            pes = int(context.args[0]) / int(context.args[2])


        txt_write(update.effective_chat.id, context.args)

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=pes)
    else:
        # если в команде не указан аргумент
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='No command argument')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='send: /kal argument')



caps_handler = CommandHandler('kal', kal)

dispatcher.add_handler(caps_handler)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('start', start)



updater.start_polling()
