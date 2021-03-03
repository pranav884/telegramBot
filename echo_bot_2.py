import logging
from telegram import Update,Bot
from flask import Flask,request
from telegram.ext import Updater,CommandHandler, MessageHandler, Filters, CallbackContext,Dispatcher
logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s-%(message)s,level=logging.INFO')
logger=logging.getLogger(__name__)
TOKEN="1680414294:AAHdHjY7pquK9f3v5OXaCRQInSRbHvXI9OI"
app=Flask(__name__)
@app.route('/')
def index():
    return "Hello"
@app.route(f'/{TOKEN}',methods=['GET','POST'])
def webhook():
    update=Update.de_json(request.get_json(),bot)
    dp.process_update(update)
    return "ok"
def start(update: Update, context: CallbackContext) -> None:
    print(update)
    author=update.message.from_user.first_name
    reply="Hi! {}".format(author)
    context.bot.send_message(chat_id=update.message.chat_id,text=reply)
def _help(update: Update, context: CallbackContext) -> None:
    help_text="Help Text"
    context.bot.send_message(chat_id=update.message.chat_id,text=help_text)
def echo_text(update: Update, context: CallbackContext) -> None:
    reply=update.message.text
    context.bot.send_message(chat_id=update.message.chat_id,text=reply)
def echo_sticker(update: Update, context: CallbackContext) -> None:
    context.bot.send_sticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)
def error(update: Update, context: CallbackContext):
    logger.error("Update'%s' caused error '%s'",update,update.error)
if __name__=="__main__":
    bot=Bot(TOKEN)
    bot.set_webhook("https://43a299027e25.ngrok.io"+TOKEN)
    dp=Dispatcher(bot,None)

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",_help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)
    app.run(port=8443)