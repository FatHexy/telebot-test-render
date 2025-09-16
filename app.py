import telebot
from google import genai

client = genai.Client(api_key="AIzaSyA8LZw-piOZ8Du8ZOYmoxJEQmbvnIfmuKs")

system_prompt = """
you are a helpful assistant that translates Inglish to French"""


# --- IMPORTANT ---
# Replace 'YOUR_API_TOKEN' with the token you got from @BotFather
API_TOKEN = '8106863748:AAHluHTF75B0i_DpXtRJuiFKvSv3xATY7Q0'
# -----------------

# Create a new bot instance
bot = telebot.TeleBot(API_TOKEN)

# --- Message Handlers ---

# Handler for the /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    This function sends a welcome message when the user sends /start or /help.
    """
    bot.reply_to(message, "Howdy, how are you doing? I am an echo bot. Just send me any message, and I will repeat it back to you!")

# Handler for all other text messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """
    This function echoes any text message that is not a command.
    """
    # The bot replies to the user's message with the exact same text.
    user_prompt = message.text
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[system_prompt, user_prompt]
    )
    
    bot.reply_to(message, response.text)


# --- Main execution ---

if __name__ == '__main__':
    print("Bot is starting...")
    # Start the bot. This function blocks the script until you stop it.
    # It continuously asks Telegram for new messages.
    # none_stop=True makes it retry even if it fails.
    bot.infinity_polling()