from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import db

async def start(update, context):
    await update.message.reply_text('Привет! Я бот-нумеролог. Напиши мне число твоего рождения, и я расскажу тебе про твой характер )')
    
async def answer(update, context):
    text = update.message.text
    if text.isnumeric() and 0 < int(text) < 32:
        num = int(text)
        answer_text = db.numeric_forecast(num)
        for i in answer_text:
            for j in i:
                await update.message.reply_text(j)
    elif (text[0].isnumeric() and text[1].isnumeric()) and 0 < int(text[:2]) < 32:
        num = int(text[:2])
        answer_text = db.numeric_forecast(num)
        for i in answer_text:
            for j in i:
                await update.message.reply_text(j)
    else:
        await update.message.reply_text('Мне не понятно! Введите просто день рождения без месяца и года.')
    