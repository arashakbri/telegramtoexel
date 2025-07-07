import telebot
import time
import requests
import traceback

TOKEN = "7868808836:AAEcnJWjL_A9GnSisUr67fXdPaQzoR4Zinw"
bot = telebot.TeleBot(TOKEN)

# حذف Webhook
try:
    response = requests.get(f"https://api.telegram.org/bot{TOKEN}/deleteWebhook")
    print("✅ Webhook حذف شد:", response.json(), flush=True)
except Exception as e:
    print("❌ خطا در حذف Webhook:", e, flush=True)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    username = message.chat.username or message.chat.first_name or "Unknown"
    text = message.text
    log = f"{username}: {text}"
    print(log, flush=True)
    bot.reply_to(message, "✅ پیام شما دریافت شد!")

print("🤖 ربات فعال شد... در حال دریافت پیام‌ها", flush=True)

while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=20, skip_pending=True)
    except Exception as e:
        print("❌ خطا:", e, flush=True)
        traceback.print_exc()
        time.sleep(15)
