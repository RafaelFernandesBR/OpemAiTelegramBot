from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import os
from OpenAI import OpenAI

token = os.environ.get('tokem')
updater = Updater(token,
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bem vindo ao bot!")


def unknown_text(update: Update, context: CallbackContext):
    text = update.message.text
    chatGPT = OpenAI()
    result = chatGPT.GetData(text)
    update.message.reply_text(result)


updater.dispatcher.add_handler(CommandHandler('start', start))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
