# Задача:

# Сбор Информации: Отправляйтесь в путь по цифровым просторам Telegram. Ваша цель – найти ID
# каждого участника учебной группы "parsinger_pyrogram", скрытые среди сообщений и активностей.

# Математическое Волшебство: С помощью созданного вами скрипта вы не просто соберёте данные.
# Вы выполните волшебный ритуал суммирования, который объединит все эти числа в одно – мощное,
# полное смысла число.

# Финальный Кодекс: Когда все ID будут собраны и сложены, перед вами предстанет число – ключ
# к завершению вашей задачи. Это число – ваш билет к победе, решение головоломки, которую вы
# только что решили.

import asyncio

from pyrogram import Client

from config import API_ID, API_HASH, GROUP_NAME


app = Client("my_session", api_id=API_ID, api_hash=API_HASH)


async def main():
    async with app:
        total_sum = 0
        async for member in app.get_chat_members(GROUP_NAME):
            total_sum += member.user.id
        print(total_sum)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
