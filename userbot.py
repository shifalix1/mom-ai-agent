from telethon import TelegramClient, events
from dotenv import load_dotenv
from ai import get_ai_reply
from memory import add_to_memory
import os
import asyncio
import random

load_dotenv()

# Load credentials from .env
API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")
PHONE = os.getenv("TELEGRAM_PHONE")

# Mumma's Telegram credentials
MUMMA = os.getenv("MUMMA_PHONE")

# Creating the userbot client
client = TelegramClient("shifali_session", API_ID, API_HASH)

# Safety feature
def is_sensitive(message):
    sensitive_words = [
        "call me",
        "urgent",
        "hospital",
        "emergency",
        "immediately",
        "come fast",
        "not well",
        "problem",
        "serious",
    ]
    message = message.lower()
    return any(word in message for word in sensitive_words)
# This dictionary tracks pending replies
pending = {}

async def delayed_reply(chat_id, message_text):
    # Wait for few minutes before replying
    await asyncio.sleep(11)
    #await asyncio.sleep(random.randint(80,180))

    # Check id still pending (Shifali hasn't replied manually)
    if chat_id in pending:
        reply = get_ai_reply(message_text)

        # Typing indicator
        async with client.action(chat_id, "typing"):
            await asyncio.sleep(min(len(reply)*0.07, 6))

        await client.send_message(chat_id, reply)
        del pending[chat_id]
        print(f"Agent replied: {reply}")

@client.on(events.NewMessage(incoming=True, from_users=MUMMA))
async def handle_mumma(event):
    message_text = event.message.text
    chat_id = event.chat_id

    # CHeck for medias
    if not message_text:
        return
    
    print(f"Mumma said: {message_text}")

    # Safety check
    if is_sensitive(message_text):
        print("Sensitive message detected - agent staying silent.")
        return

    # Cancel previous timer if mumma sends another message
    if chat_id in pending:
        pending[chat_id].cancel()

    # Start new timer
    task = asyncio.create_task(delayed_reply(chat_id, message_text))
    pending[chat_id] = task

@client.on(events.NewMessage(outgoing=True))
async def handle_my_reply(event):

    # If Shifali replies manually, cancel the agent timer
    print("Shifali replied manually, cancelling agent...")

    for task in pending.values():
        task.cancel()   # Cancel the task

    pending.clear()     # Empty the dictionary

async def main():
    await client.start(phone=PHONE)
    print("Userbot is running as Shifali!")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
