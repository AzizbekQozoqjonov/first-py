import telebot

bot = telebot.TeleBot("5660911106:AAF5WTcbggKZHhEhB3yMXUu9z8j709BpHN4")

@bot.message_handler(commands=["start"])
def worker(mess):
          bot.send_message(mess.chat.id, "Salom")

bot.infinity_polling()




