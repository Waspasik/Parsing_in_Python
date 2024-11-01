# Задача:

# Погружение в Глубины: Ваша первая задача - нырнуть в цифровые глубины и извлечь информацию из
# поля "description" учебной группы "parsinger_pyrogram". Это поле скрывает в себе текст, полный
# различных символов, среди которых скрыты настоящие жемчужины - четные цифры.

# Очистка от Лишнего: После того как информация будет извлечена, наступит время для второго
# этапа - процесса очистки. Вам предстоит отсеять все лишнее, оставив только четные цифры
# больше нуля.

from pyrogram import Client

from config import API_ID, API_HASH, GROUP_NAME


app = Client("my_session", api_id=API_ID, api_hash=API_HASH)


def main():
    with app:
        chat = app.get_chat(chat_id=GROUP_NAME)
        description = chat.description
        nums = "".join((i for i in description if i.isdigit() and int(i) % 2 == 0 and int(i) > 0))
        print(nums)


main()
