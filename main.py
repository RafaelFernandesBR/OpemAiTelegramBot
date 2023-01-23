from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import os
import openai

token = os.environ.get('tokem')
OpemAiToken = os.environ.get('opemAItokem')
updater = Updater(token,
                  use_context=True)
openai.api_key = OpemAiToken


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bem vindo ao bot!")


def unknown_text(update: Update, context: CallbackContext):
    text = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5
    )
    update.message.reply_text(response["choices"][0]["text"])


updater.dispatcher.add_handler(CommandHandler('start', start))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
