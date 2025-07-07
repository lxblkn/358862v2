import asyncio
from telethon import TelegramClient, events
from env_vars import API_ID, API_HASH, PHONE_NUMBER, SOURCE_CHAT_IDS, TARGET_GROUP_ID, KEYWORDS
from datetime import datetime
import pytz

moscow = pytz.timezone("Europe/Moscow")
client = TelegramClient(PHONE_NUMBER, API_ID, API_HASH)

def message_contains_keywords(message_text):
    if not message_text:
        return False
    lower_text = message_text.lower()
    return any(keyword.lower() in lower_text for keyword in KEYWORDS)

@client.on(events.NewMessage(chats=SOURCE_CHAT_IDS))
async def handler(event):
    now = datetime.now(moscow)
    print(f"[{now.strftime('%H:%M:%S')}] Получено сообщение: {event.message.text}")  # DEBUG print

    if now.hour < 11 and now.hour >= 1:
        print("⏰ Вне рабочего времени, сообщение проигнорировано")
        return

    if event.message.text and message_contains_keywords(event.message.text):
        sender = await event.get_sender()
        chat = await event.get_chat()

        message_link = None
        if hasattr(event.message, 'id') and hasattr(chat, 'username') and chat.username:
            message_link = f"https://t.me/{chat.username}/{event.message.id}"

        result = f"📢 **Сообщение из чата:** {getattr(chat, 'title', 'Без названия')}\n"
        if sender.username:
            result += f"👤 @{sender.username}\n"
        if message_link:
            result += f"🔗 [Открыть сообщение]({message_link})\n"
        result += f"\n📝 {event.message.text}"

        await client.send_message(TARGET_GROUP_ID, result, link_preview=False)
        print("✅ Отправлено в целевую группу")

async def main():
    await client.start()
    print("✅ Парсер запущен. Слушаю чаты...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
