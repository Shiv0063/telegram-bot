from telegram.ext import * 

from telegram import InputMediaPhoto
from telegram.ext import Updater
from django.db.models import Max
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

API_KEY = '5981089563:AAGBtnsxV2pvZ-HbkBS9hmUuOs4CmDuTO4k'



async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello vishal')

async def vish(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello ')

def val(update,context):
    return update.message.reply_text(f"i'm chat bot")

def start(update,context):
    return update.message.reply_text(f""" hello i'm""")



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    value=update['message']['chat']['username']
    text = str(update.message.text).lower()
    txt={
        'hii':"hii i'm your bot...",
        'hello':"hello i'm your bot...",
        "vishal":"hiii vishal",
        'value':value,
        "customers":"1",
        "prodect":"1",
        "customer name":"1",
    }
    for i in txt.keys():
        if text==i:
            await update.message.reply_text(txt[i])


app = ApplicationBuilder().token(API_KEY).build()

app.add_handler(CommandHandler("hii",val))
app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("yes",vish))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()