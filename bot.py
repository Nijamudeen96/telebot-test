# This is a test for a workshop
# Therefore there will be many comments

# imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

# variables
updater = Updater(token='1026442786:AAHb7k-DB4EnXdW58ZiZC09q80YLzFvJfbI', use_context=True)
dispatcher = updater.dispatcher

# functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Oh hey there handsome!")
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)    
def setdate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="tell me what you want bebeh")
def horo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Lemme tell you smth")    
# main
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

date_handler = CommandHandler('setdate', setdate)
dispatcher.add_handler(date_handler)

horo_handler = CommandHandler('horoscope', horo)
dispatcher.add_handler(horo_handler)

updater.start_polling()
print('bot is working')