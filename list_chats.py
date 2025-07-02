from telethon.sync import TelegramClient

api_id = 22025976
api_hash = '242315e1e6f5fea64fd1e065919ff6d1'
phone_number = '+17653032671'

with TelegramClient(phone_number, api_id, api_hash) as client:
    print("✅ Авторизация прошла успешно.")
