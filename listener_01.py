from telethon.sync import TelegramClient, events
from env_vars import *
import asyncio

client = TelegramClient(PHONE_NUMBER, API_ID, API_HASH)

async def main():
    async with client:
        @client.on(events.NewMessage(chats=SOURCE_CHAT_IDS))
        async def handler(event):
            text = event.message.message.lower()
            if any(keyword in text for keyword in KEYWORDS):
                chat = await event.get_chat()
                sender = await event.get_sender()

                chat_name = getattr(chat, 'title', 'Unknown Chat')
                chat_username = getattr(chat, 'username', None)
                sender_username = getattr(sender, 'username', None)
                message_id = event.message.id

                link = f"https://t.me/{chat_username}/{message_id}" if chat_username else "Ссылка недоступна"

                response = f"📌 *Найдено сообщение:*\n"
                response += f"👥 Чат: {chat_name}\n"
                response += f"🙋‍♂️ Пользователь: @{sender_username if sender_username else 'Неизвестен'}\n"
                response += f"🔗 Ссылка: {link}\n"
                response += f"💬 Текст: {event.message.message}"

                await client.send_message(int(TARGET_GROUP_ID), response)

        print("Слушаю чаты...")
        await client.run_until_disconnected()

asyncio.run(main())
