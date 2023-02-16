# Задача:

# Спарсить числовые значения из сообщений в группе 'https://t.me/Parsinger_Telethon_Test';
# Суммировать полученные числа.

from telethon import TelegramClient, events, sync, connection


api_id = 1111111
api_hash = 'hash'

with TelegramClient('my', api_id, api_hash) as client:
    total = 0

    for message in client.iter_messages('https://t.me/Parsinger_Telethon_Test'):
        try:
            if message.message.isdigit():
                total += int(message.message)
        except AttributeError:
            continue
    
    print(total)



# Задача:

# В группе 'https://t.me/Parsinger_Telethon_Test' есть закреплённое сообщение;
# Цель: получить user_id пользователя чьё сообщение закреплено.

from telethon import TelegramClient, events, sync, connection
from telethon.tl.types import InputMessagesFilterPinned


api_id = 1111111
api_hash = 'hash'

with TelegramClient('my', api_id, api_hash) as client:
    for message in client.get_messages('https://t.me/Parsinger_Telethon_Test', filter=InputMessagesFilterPinned):
        print(message.from_id.user_id)



# Задача:

# В группе 'https://t.me/Parsinger_Telethon_Test' пользователь с user_id=5807015533 оставил
# несколько цифровых сообщений;
# Цель: Определить участника с указанным user_id и получить его сообщения и суммировать их.

from telethon import TelegramClient, events, sync, connection


api_id = 1111111
api_hash = 'hash'

with TelegramClient('my', api_id, api_hash) as client:
    user_id = 5807015533
    result = 0

    for message in client.iter_messages('https://t.me/Parsinger_Telethon_Test', from_user=user_id):
        try:
            result += int(message.message)
        except (AttributeError, ValueError):
            continue

    print(result)



# Задача:

# Цель: собрать username всех пользователей которые отправили числовое сообщение в группу
# 'https://t.me/Parsinger_Telethon_Test';
# Создать список из этих username;
# Ожидаемый список (символ @ добавлять к username не нужно), в списке может быть только 1
# username пользователя. Если у пользователя отсутствует username, исключить его из списка.

from telethon import TelegramClient, events, sync, connection


api_id = 1111111
api_hash = 'hash'

with TelegramClient('my', api_id, api_hash) as client:
    users = set()

    for message in client.iter_messages('https://t.me/Parsinger_Telethon_Test'):
        try:
            if message.message.isdigit():
                id_user = message.from_id.user_id
                users.add(client.get_entity(id_user).username)
        except (AttributeError, ValueError):
            continue

    print(list(users))



# Задача:

# Скачайте все изображения из группы 'https://t.me/Parsinger_Telethon_Test';
# Определите общий размер всех фотографий.

from os.path import getsize
from telethon import TelegramClient, events, sync, connection
from telethon.tl.types import InputMessagesFilterPhotos


api_id = 1111111
api_hash = 'hash'

with TelegramClient('my', api_id, api_hash) as client:
    total_size = 0

    for message in client.iter_messages('https://t.me/Parsinger_Telethon_Test', filter=InputMessagesFilterPhotos):
        photo = client.download_media(message.media, file='img')
        total_size += getsize(photo)
        
    print(total_size)