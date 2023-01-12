# Задача:

# Перейдите на сайт https://parsinger.ru/img_download/index.html
# На 1 из 160 картинок написан секретный код
# Напишите код, который поможет вам скачать все картинки
# В скачанных картинках найдите вручную секретный код
# Вставьте код в поле для ответа

import requests
import os

url = 'https://parsinger.ru/img_download/index.html'
response = requests.get(url=url, stream=True)
file_status = {}

for i in range(1, 161):
    response = requests.get(url=f'https://parsinger.ru/img_download/img/ready/{i}.png')
    with open(f'D:/Python/Parsing/pictures/image{i}.png', 'wb') as picture:
        picture.write(response.content)
    file_size = os.stat(f'D:/Python/Parsing/pictures/image{i}.png').st_size
    file_status[file_size] = file_status.get(file_size, 0) + 1

unique_image_size = min(file_status.items(), key=lambda item: item[1])[0]

for i in range(1, 161):
    if os.stat(f'D:/Python/Parsing/pictures/image{i}.png').st_size == unique_image_size:
        print(f'В изображении с названием "image{i}.png" находится секретный код.')
        break
    else:
        continue