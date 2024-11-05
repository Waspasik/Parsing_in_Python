# Арифметика цифрового мира

# 1. В учебной группе "parsinger_pyrogram" некоторые сообщения таят в себе числа, которые
# нужно умножить на уникальный ID.

# 2. Ваша задача - написать скрипт, который обнаружит каждое число и его ID, затем умножит
# их, ведь именно в этом действии кроется магия раскрытия их истинной силы.

# 3. После того как вы умножите каждое число на его ID, вам нужно будет сложить полученные
# результаты. Эта сумма и станет ключом к разгадке, финальным числом, которое укажет на
# успешное завершение вашего задания.

import asyncio

from pyrogram import Client

from config import API_ID, API_HASH, GROUP_NAME


app = Client("my_session", api_id=API_ID, api_hash=API_HASH)


async def main():
    async with app:
        total_sum = 0
        async for message in app.get_chat_history(GROUP_NAME):
            if message.text:
                if message.text.isdigit():
                    total_sum += int(message.text) * message.id
            elif message.caption:
                if message.caption.isdigit():
                    total_sum += int(message.caption) * message.id

        print(total_sum)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



# Поиск ID в сообщенях с ссылкой

# 1. Экспедиция в чат: Погрузитесь в архивы чата "parsinger_pyrogram", где среди многочисленных
# сообщений скрываются те самые, оживленные GIF-ами.

# 2. Открытие GIF-сообщений: Определите сообщения, которые содержат в себе эти веселые анимации.
# Это важная находка на вашем пути.

# 3. Расшифровка идентификаторов: Каждое сообщение и пользователь несут в себе уникальный код — ID.
# Отправляйтесь на поиски и определите ID пользователей, которые поделились этими GIF-ами.

# 4. Формула Открытия: Каждый найденный ID пользователя умножьте на ID соответствующего сообщения.
# Это ваш второй шаг к цели.

# 5. Ключевая Сумма: Сложите все получившиеся произведения вместе. Получившееся число — не просто
# сумма. Это ключ к решению задачи, загадочный код, открывающий последний замок на пути к победе.

import asyncio

from pyrogram import Client
from pyrogram.enums import MessagesFilter

from config import API_ID, API_HASH, GROUP_NAME


app = Client(name="my_session", api_id=API_ID, api_hash=API_HASH)


async def main():
    async with app:
        total_sum = 0
        async for message in app.search_messages(chat_id=GROUP_NAME, filter=MessagesFilter.ANIMATION):
            total_sum += message.from_user.id * message.id
        
        print(total_sum)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



# Подсчёт символов в закрепах

# 1. Вход в Чат: Войдите в учебный чат "parsinger_pyrogram", где история знаний удерживается в 
# виде закреплённых сообщений.

# 2. Изучение Закрепов: Исследуйте каждое закреплённое сообщение, как будто оно - древний
# манускрипт, хранящий секретные знания.

# 3. Подсчёт Символов: Аккуратно подсчитайте количество символов в каждом из этих сообщений.
# Обратите внимание, что пробелы - это лишь пустота между словами знаний, их считать не следует.

# 4. Сложение Чисел: Сложите все полученные числа, чтобы получить окончательное число, которое
# является ключом к решению этой задачи.

import asyncio

from pyrogram import Client
from pyrogram.enums import MessagesFilter

from config import API_ID, API_HASH, GROUP_NAME


app = Client(name="my_session", api_id=API_ID, api_hash=API_HASH)


async def main():
    async with app:
        total_sum = 0
        async for message in app.search_messages(chat_id=GROUP_NAME, filter=MessagesFilter.PINNED):
            if message.text:
                total_sum += len(message.text.replace(" ", ""))
            elif message.caption:
                total_sum += len(message.caption.replace(" ", ""))
        
        print(total_sum)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



# Поиск "Спящего" пользователя

# 1. Миссия: Ваша миссия состоит в том, чтобы исследовать данные пользователей и определить,
# кто из них дольше всех не появлялся в сети (online) в учебной группе "parsinger_pyrogram".

# 2. Инструменты детектива: Вам предстоит проанализировать поля last_online_date в объектах
# сообщений пользователей. Эти поля содержат информацию о последнем времени их появления
# онлайн.

# 3. Цель расследования: Найдите пользователя с самой давней датой в поле last_online_date.
# ID этого пользователя и будет ключом к решению задачи.

import asyncio

from pyrogram import Client

from config import API_ID, API_HASH, GROUP_NAME


app = Client(name="my_session", api_id=API_ID, api_hash=API_HASH)


async def main():
    async with app:
        user_ids = {}
        async for message in app.get_chat_history(chat_id=GROUP_NAME):
            try:
                if message.from_user.last_online_date:
                    user_ids[message.from_user.id] = message.from_user.last_online_date
            except AttributeError:
                continue
        
        print(min(user_ids, key=user_ids.get))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



# Разгадка обсуждения в учебной группе

# 1. Ваша миссия начинается в учебной группе "parsinger_pyrogram". Внимательно изучите объект
# сообщения, в частности, поле reply_to_message_id, которое играет ключевую роль в решении
# этой задачи.

# 2. На основе поля reply_to_message_id, выявите все сообщения на которые пользователи оставляли
# свои "ответы"

# 3. После того как вы определите все такие сообщения, приступайте к суммированию всех уникальных
# ID пользователей — авторов этих сообщений, т.е. вам необходимо обработать только родительские
# сообщения (на изображении выделено красным). Будьте внимательны, у одного автора может быть
# несколько сообщений!

# 4. Введите полученное значение суммы ID всех авторов "родительских" сообщений в поле ответа.

import asyncio

from pyrogram import Client

from config import API_ID, API_HASH, GROUP_NAME


app = Client(name="my_session", api_id=API_ID, api_hash=API_HASH)


async def main():
    async with app:
        message_ids = []
        async for message in app.get_chat_history(chat_id=GROUP_NAME):
            if message.reply_to_message_id:
                message_ids.append(message.reply_to_message_id)
        
        reply_messages = await app.get_messages(chat_id=GROUP_NAME, message_ids=message_ids)
        unique_user_ids = set()
        for message in reply_messages:
            try:
                unique_user_ids.add(message.from_user.id)
            except AttributeError:
                continue
        
        print(sum(unique_user_ids))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
