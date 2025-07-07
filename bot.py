import telebot
import time

TOKEN = "7761459100:AAH5CQ8-EPVkKK4wNCBdkS9MCebpnR8GI_4"
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
