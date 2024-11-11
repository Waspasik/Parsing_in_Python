# Тихие наблюдатели в чате

# 1. Миссия Разведки: Ваша задача состоит в том, чтобы идентифицировать этих "тихих наблюдателей"
# в учебной группе "parsinger_pyrogram". Они характеризуются тем, что не вступают в обсуждения.
# (необходимо найти среди пользователей тех, кто не отправил ни одного сообщения в чат)

# 2. Сбор Данных: Проанализируйте активность пользователей в группе, выявляя тех, кто соответствует
# критерию "тихого наблюдателя". Извлеките их уникальные ID.

# 3. Математика Слежения: После того как вы соберете список ID, ваша следующая задача - суммировать
# эти числа.

# 4. Отчёт о Задании: Представьте сумму ID в качестве ответа на задачу. Это число и будет вашим
# ключом к разгадке и показателем вашей внимательности и аналитических способностей.

import asyncio

from pyrogram import Client

from config import API_ID, API_HASH, GROUP_NAME


async def main():
    async with Client(name="my_session", api_id=API_ID, api_hash=API_HASH) as app:
        messages = app.get_chat_history(GROUP_NAME)
        chat_member_ids = set()
        async for message in messages:
            try:
                chat_member_ids.add(message.from_user.id)
            except AttributeError:
                continue
        
        total = 0
        async for member in app.get_chat_members(GROUP_NAME):
            if member.user.id not in chat_member_ids:
                total += member.user.id
        
        print(total)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



# Гармония чётности 

# 1. Цель Исследования: Ваша задача - обработать сообщения в учебной группе "parsinger_pyrogram",
# используя уникальную математическую формулу.

# 2. Критерии Отбора и Обработки:
# Отфильтруйте сообщения, у которых ID пользователя и ID сообщения - чётные числа, а количество
# символов в сообщении - тоже чётное число. Перед подсчетом символов в сообщении удалите из него
# все пробельные символы.

# 3. Математическая Формула Результата:
# Примените следующую формулу вычисления итогового значения для каждого отобранного сообщения:
# result = (USER_ID * MESSAGE_ID * len(MESSAGE)), где:
# USER_ID - Чётное ID пользователя.
# MESSAGE_ID - Чётное  ID сообщения.
# len(MESSAGE) - Чётная длина текста сообщения после удаления пробелов.

# 4. Финальный Шаг:
# Суммируйте результаты вычислений для каждого отобранного сообщения.
# Вставьте итоговую сумму в поле для ответа.

import asyncio

from pyrogram import Client
from pyrogram.types import Message

from config import API_ID, API_HASH, GROUP_NAME


async def math_formula(message: Message) -> int:
    return message.from_user.id * message.id * len(message.text.replace(" ", ""))


async def parity_check(message: Message) -> bool:
    if message.text and message.from_user.id % 2 == 0 and message.id % 2 == 0 and len(message.text.replace(" ", "")) % 2 == 0:
        return True
    return False


async def main() -> None:
    async with Client(name="my_session", api_id=API_ID, api_hash=API_HASH) as app:
        total = 0
        messages = app.get_chat_history(GROUP_NAME)
        async for message in messages:
            if await parity_check(message):
                total += await math_formula(message)

        print(total)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



# Цифровой вес всех аватаров

# 1. Сбор Аватаров: Ваша первая задача - скачать аватарки всех участников учебной группы
# "parsinger_pyrogram". 

# 2. Анализ Объема Данных: После скачивания аватаров используйте предложенную функцию
# calculate_directory_size для определения общего размера скачанных файлов в байтах.

# 3. Отчет о Результатах: Вставьте полученный общий размер аватарок в поле ответа на степик.

import asyncio
import os

from pyrogram import Client
from pyrogram.types import ChatMember

from config import API_ID, API_HASH, GROUP_NAME


async def calculate_directory_size(path: str) -> int:
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


async def downloader(app: Client, member: ChatMember, path: str) -> None:
    chat_member_photos = app.get_chat_photos(member.user.id)
    async for photo in chat_member_photos:
        await app.download_media(photo, file_name=f"{path}{member.user.photo.big_photo_unique_id}.jpg")


async def main() -> None:
    async with Client(name="my_session", api_id=API_ID, api_hash=API_HASH) as app:
        path = "media/"
        tasks = [
            downloader(app, member, path)
            async for member in app.get_chat_members(GROUP_NAME)
        ]
        await asyncio.gather(*tasks)
        result = await calculate_directory_size(path)

        print(result)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
