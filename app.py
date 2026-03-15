from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os
load_dotenv()

# This function runs everytime a message is received
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Get the text of the incoming message
    message_text = update.message.text

    # Get the sender's name
    sender_name = update.message.from_user.first_name

    # Print both to terminal
    print(f"Meessage from {sender_name}: {message_text}")

# Building the bot application using token
TOKEN = os.getenv("TELEGRAM_TOKEN")
app = ApplicationBuilder().token(TOKEN).build()

# Tell the bot- When a text message arrives, call handle_message
app.add_handler(MessageHandler(filters.TEXT, handle_message))

# START THE BOT
print("Bot is running...")
app.run_polling()