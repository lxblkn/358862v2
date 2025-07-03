import asyncio
from telethon import TelegramClient, events
from env_vars import API_ID, API_HASH, PHONE_NUMBER, SOURCE_CHAT_IDS, TARGET_GROUP_ID, KEYWORDS
from datetime import datetime
import pytz

SOURCE_CHAT_IDS = [-1234567890, -100987654321]

# Устанавливаем часовой пояс на Москву
moscow = pytz.timezone("Europe/Moscow")
client = TelegramClient(PHONE_NUMBER, API_ID, API_HASH)

def message_contains_keywords(message_text):
    lower_text = message_text.lower()
    return any(keyword.lower() in lower_text for keyword in KEYWORDS)

@client.on(events.NewMessage(chats=SOURCE_CHAT_IDS))
async def handler(event):
print(f"[DEBUG] Получено сообщение: {event.message.text}")
  now = datetime.now(moscow)
    if now.hour < 11 or now.hour >= 1:
        return  # вне времени работы

    if event.message.text and message_contains_keywords(event.message.text):
        sender = await event.get_sender()
        chat = await event.get_chat()
        message_link = None

        if hasattr(event.message, 'id') and hasattr(chat, 'username') and chat.username:
            message_link = f"https://t.me/{chat.username}/{event.message.id}"

        # Формируем сообщение
        result = f"📢 **Сообщение из чата:** {getattr(chat, 'title', 'Без названия')}\n"
        if sender.username:
            result += f"👤 @{sender.username}\n"
        if message_link:
            result += f"🔗 [Открыть сообщение]({message_link})\n"
        result += f"\n📝 {event.message.text}"

        await client.send_message(TARGET_GROUP_ID, result, link_preview=False)

async def main():
    await client.start()
    print("✅ Парсер запущен. Слушаю чаты...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
