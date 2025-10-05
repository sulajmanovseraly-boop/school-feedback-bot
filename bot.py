import telebot

# Use your token here
bot = telebot.TeleBot("8478347349:AAFwYo4-W9k4K19MfRM9gTiITja0VbEXCkE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Your bot is working!")

bot.infinity_polling()
