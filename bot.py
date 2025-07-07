import telebot
import time

TOKEN = "7868808836:AAEcnJWjL_A9GnSisUr67fXdPaQzoR4Zinw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    username = message.chat.username or message.chat.first_name or "Unknown"
    text = message.text
    log = f"{username}: {text}"
    print(log)  # ← این خط پیام رو توی لاگ GitHub چاپ می‌کنه
    bot.reply_to(message, "✅ پیام شما دریافت شد!")

print("ربات فعال شد...")

while True:
    try:
        bot.polling()
    except Exception as e:
        print("خطا:", e)
        time.sleep(15)
