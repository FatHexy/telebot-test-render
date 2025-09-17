# In a file like api/index.py

import os
import telebot
from flask import Flask, request

# --- Configuration ---
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# --- Bot Logic ---
# This is the endpoint Telegram will send updates to
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    else:
        return 'Bad Request', 400

# Simple start handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello from Vercel! I am a webhook-powered bot.")

# A simple echo handler
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
