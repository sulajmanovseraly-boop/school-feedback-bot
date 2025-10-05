import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Отправь своё предложение или жалобу — я передам президенту школы. Всё анонимно 👀")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    with open("feedback.txt", "a", encoding="utf-8") as f:
        f.write(f"{message.text}\n---\n")
    bot.reply_to(message, "✅ Спасибо! Сообщение отправлено анонимно.")

bot.infinity_polling()
