import os
import telebot

# Pulls your token securely from GitHub Secrets
BOT_TOKEN = os.environ.get('README_BOT')
bot = telebot.TeleBot(BOT_TOKEN)

# Replace 'YOUR_TELEGRAM_CHAT_ID' with your actual numeric Telegram chat ID
# (You can get your ID by messaging @userinfobot on Telegram)
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID" 

try:
    bot.send_message(CHAT_ID, "🤖 Hello! This is an automated update from your GitHub Actions workflow.")
    print("Message sent successfully!")
except Exception as e:
    print(f"Error sending message: {e}")
