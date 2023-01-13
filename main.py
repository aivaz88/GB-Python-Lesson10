from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler
import commands
from config import TOKEN

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", commands.start))
app.add_handler(MessageHandler(filter.__text_signature__, callback=commands.answer))

print('server start')
app.run_polling() 