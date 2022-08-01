from urllib import response

from tables import Filters
import Constants as keys
from telegram.ext import *

import Responses as R

print("Bot Started")

def start_command(update, context):
    update.message.replay_text("Hey its started")

def hamdle_message(update , context):
    text = dtr(update.message.text).lower()
    response - R.Respo(text)
    update.message.replay_text(response)

def error(update , context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    
    dp.add_handler(MessageHandler(Filters.text,hamdle_message))

    dp.add_handler(error)

    updater.start_polling(0)
    updater.idle()

main()
    