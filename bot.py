import telebot
import openpyxl
import os

bot = telebot.TeleBot(os.environ["7761459100:AAH5CQ8-EPVkKK4wNCBdkS9MCebpnR8GI_4"])

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        wb = openpyxl.load_workbook("data.xlsx")
        ws = wb.active
        username = message.chat.username or message.chat.first_name or "Unknown"
        text = message.text
        ws.append([username, text])
        wb.save("data.xlsx")
        bot.reply_to(message, "✅ پیام شما ذخیره شد!")
    except Exception as e:
        bot.reply_to(message, f"❌ خطا: {e}")

bot.polling()