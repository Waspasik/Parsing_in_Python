# Фото экспедиция в учебную группу

# 1. Сбор Изображений: Напишите скрипт на Pyrogram, чтобы скачать все изображения
# из нашей учебной группы.

# 2. Хранение и Организация: Сохраните все изображения в одной директории на вашем
# компьютере, удостоверившись, что каждое изображение было успешно загружено (.png
# или .jpg).

# 3. Вычисление Общего Размера: Примените функцию calculate_directory_size к
# директории с изображениями, чтобы подсчитать общий размер файлов в байтах.

# 4. Финальный Шаг: Предоставьте общий размер файлов изображений как решение задачи.

import asyncio
import os

from pyrogram import Client
from pyrogram.enums import MessagesFilter

from config import API_ID, API_HASH, GROUP_NAME


async def calculate_directory_size(path):
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


async def downloader(app, message, path):
    await app.download_media(message, file_name=f"{path}{message.photo.file_size}.jpg")


async def main():
    async with Client(name="my_session", api_id=API_ID, api_hash=API_HASH) as app:
        path = "media/"
        tasks = [
            downloader(app, message, path)
            async for message in app.search_messages(chat_id=GROUP_NAME, filter=MessagesFilter.PHOTO)
        ]
        await asyncio.gather(*tasks)
        result = await calculate_directory_size(path)
        print(result)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
