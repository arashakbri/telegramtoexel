import telebot
import time
import requests
import traceback

TOKEN = "7868808836:AAEcnJWjL_A9GnSisUr67fXdPaQzoR4Zinw"
bot = telebot.TeleBot(TOKEN)

# حذف Webhook
try:
    response = requests.get(f"https://api.telegram.org/bot{TOKEN}/deleteWebhook")
    print("Webhook حذف شد:", response.json())
except Exception as e:
    print("خطا در حذف Webhook:", e)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    username = message.chat.username or message.chat.first_name or "Unknown"
    text = message.text
    log = f"{username}: {text}"
    print(log)
    bot.reply_to(message, "✅ پیام شما دریافت شد!")

print("ربات فعال شد...")

while True:
    try:
        bot.polling()
    except Exception as e:
        print("خطا:", e)
        traceback.print_exc()
        time.sleep(15)
