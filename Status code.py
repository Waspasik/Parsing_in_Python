# Задача

# Откройте сайт https://parsinger.ru/task/1/
# На нём есть 500 ссылок  и только 1 вернёт статус код 200
# Напишите код который поможет найти правильную ссылку
# По этой ссылке лежит секретный код, который необходимо вставить в поле ответа.

import requests

url = 'https://parsinger.ru/task/1/'
for i in range(1, 501):
    response = requests.get(url=f'{url}/{i}.html')
    if response.status_code == 200:
        print(response.text)
        break
    else:
        continue