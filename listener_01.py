from env_vars import *
import os
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE_NUMBER")
target_group = int(os.getenv("TARGET_GROUP_ID"))
source_chats = os.getenv("SOURCE_CHAT_IDS").split(",")
keywords = [kw.strip().lower() for kw in os.getenv("KEYWORDS").split(",")]

client = TelegramClient("session_listener_01", api_id, api_hash)

@client.on(events.NewMessage(chats=source_chats))
async def handler(event):
    msg = event.message.message.lower()
    if any(keyword in msg for keyword in keywords):
        await client.send_message(target_group, event.message)

async def main():
    await client.start(phone=phone)
    print("Listener started.")
    await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
