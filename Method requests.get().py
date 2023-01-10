# Задача:

# Перейдите на сайт https://parsinger.ru/video_downloads/
# Скачайте видео с сайта  при помощи requests
# Определите его размер в ручную
# Напишите размер файла в поле для ответа. Написать нужно только цифру в мегабайтах

import requests
import os


url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'
response = requests.get(url=url, stream=True)
with open('D:/Python/Parsing/music.mp4', 'wb') as file:
    file.write(response.content)

print(os.stat('D:/Python/Parsing/music.mp4').st_size / 1024 / 1024)