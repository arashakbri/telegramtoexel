import telebot
import time
import requests
import traceback
import os
import sys
import atexit

TOKEN = "7868808836:AAEcnJWjL_A9GnSisUr67fXdPaQzoR4Zinw"
bot = telebot.TeleBot(TOKEN)

print("🔁 در حال بررسی اجرای همزمان...")

# جلوگیری از اجرای همزمان
pid_file = "bot.lock"
if os.path.exists(pid_file):
    print("⚠️ اجرای قبلی هنوز فعاله. خروج...")
    sys.exit()
else:
    with open(pid_file, "w") as f:
        f.write("running")

# حذف فایل قفل در پایان اجرا
def remove_lock():
    if os.path.exists(pid_file):
        os.remove(pid_file)
atexit.register(remove_lock)

# حذف Webhook
try:
    response = requests.get(f"https://api.telegram.org/bot{TOKEN}/deleteWebhook")
    print("✅ Webhook حذف شد:", response.json())
except Exception as e:
    print("❌ خطا در حذف Webhook:", e)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    username = message.chat.username or message.chat.first_name or "Unknown"
    text = message.text
    log = f"{username}: {text}"
    print(log)
    bot.reply_to(message, "✅ پیام شما دریافت شد!")

print("🤖 ربات فعال شد... در حال دریافت پیام‌ها")

while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=20, skip_pending=True)
    except Exception as e:
        print("❌ خطا:", e)
        traceback.print_exc()
        time.sleep(15)
