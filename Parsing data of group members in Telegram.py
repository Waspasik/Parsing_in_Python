# Задача:

# Получить список всех участников группы 'https://t.me/Parsinger_Telethon_Test';
# Извлечь у каждого подписчика first_name и last_name.

from telethon import TelegramClient


api_id = 1111111
api_hash = 'hash'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
print([' '.join((item.first_name, item.last_name)) for item in client.get_participants('https://t.me/Parsinger_Telethon_Test')])
client.disconnect()



# Задача:

# Получить данные участников группы 'https://t.me/Parsinger_Telethon_Test';
# id
# first_name
# last_name
# phone

from telethon import TelegramClient


api_id = 1111111
api_hash = 'hash'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
print([f'{item.id} {item.first_name} {item.last_name} {item.phone}'
       for item in client.get_participants('https://t.me/Parsinger_Telethon_Test')])
client.disconnect()



# Задача:

# Скачайте полноразмерные аватарки всех участников группы 'https://t.me/Parsinger_Telethon_Test';
# Узнайте размер всех фотографий участников группы.

from os.path import getsize
from telethon import TelegramClient


api_id = 1111111
api_hash = 'hash'

with TelegramClient('my', api_id, api_hash) as client:
    total_size = 0
    participants = client.get_participants('t.me/Parsinger_Telethon_Test')
    for i, user in enumerate(participants):
        client.download_profile_photo(user, f'{i}', download_big=True)
        total_size += getsize(f'{i}.jpg')
    print(total_size)



# Задача:

# Скачайте полноразмерные аватарки всех участников группы 'https://t.me/Parsinger_Telethon_Test'
# включая все сохранённые аватарки;
# Встроенной функцией в windows, узнайте общий размер всех аватарок.
# Узнайте размер всех фотографий участников группы.

from os.path import getsize
from telethon import TelegramClient


api_id = 1111111
api_hash = 'hash'

with TelegramClient('my', api_id, api_hash) as client:
    total_size = 0
    user_index = 0
    participants = client.get_participants('t.me/Parsinger_Telethon_Test')
    
    for user in participants:
        short_file_name = f'user{user_index}'
        photo_index = 1
        for photo in client.iter_profile_photos(user):
            full_file_name = f'{short_file_name + str(photo_index)}.jpg'
            client.download_media(photo, file=f'{full_file_name}')
            total_size += getsize(full_file_name)
            photo_index += 1
        user_index += 1

    print(total_size)



# Задача:

# Есть список lst=[] в котором хранятся ID участников группы 'https://t.me/Parsinger_Telethon_Test';
# Цель собрать числа из поля "О Себе" или "About" пользователя если его ID имеется в списке,
# затем суммировать все добытые числа.

from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest


api_id = 1111111
api_hash = 'hash'
lst = [332703068, 5914813738, 5710963988, 5799970696, 5843185336, 
       5899028303, 5799846345, 5988909155, 5765618528, 5744269105,
       5811870581, 5749394385, 5821321049, 5831778721, 5908359516, 
       5807015533, 5877375636, 5748959968, 5852187682, 5642780248, 
       5633717169, 5989940172]

with TelegramClient('my', api_id, api_hash) as client:
    users = client.iter_participants('https://t.me/Parsinger_Telethon_Test')
    print(sum(int(client(GetFullUserRequest(user)).full_user.about) for user in users if user.id in lst))



# Задача:

# Есть список lst=[] в котором хранятся username участников группы 'https://t.me/Parsinger_Telethon_Test';
# Цель собрать числа из поля "О Себе" или "About" пользователя из списка lst=[], затем суммировать все добытые числа.

from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest


api_id = 1111111
api_hash = 'hash'
lst = ['Anthony_Hills', 'Craig_Moody', 'Kathleen_Browns', 'Vicki_Baileys', 'Jorge_Garrett',
       'Larry_Summers', 'Tommy_Sullivan', 'Edward_Murrray', 'Nicholas_Gonzales', 'Virgina_Garcia',
       'Denise_Barker', 'Jessie_Wright', 'Mary_Baileyn', 'Claytons_Riley', 'Joshuan_Chandler', 
       'Jameson_Powell', 'Harry_Valdes', 'Chriss_Yong', 'Sarah_Wilis', 'Frances_Ross',
       'Joseph_Anderson']

with TelegramClient('my', api_id, api_hash) as client:
    users = client.iter_participants('https://t.me/Parsinger_Telethon_Test')
    print(sum(int(client(GetFullUserRequest(user)).full_user.about) for user in users if user.username in lst))