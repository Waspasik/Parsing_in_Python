# Магистраль Знаний:

# 1. Откройте чат учебной группы "parsinger_pyrogram", где ведётся активное обсуждение различных
# тем. Ваша цель - написать скрипт, чтобы найти все числовые значения. 

# 2. Собрав все числа, суммируйте их. Сумма чисел и будет ключом для решения задачи.

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
                    total_sum += int(message.text)
            elif message.caption:
                if message.caption.isdigit():
                    total_sum += int(message.caption)

        print(total_sum)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
