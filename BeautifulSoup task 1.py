# Задача:

# Скачайте по ссылке https://parsinger.ru/downloads/cooking_soup/index.zip zip-архив вручную
# Распакуйте его в папку с вашим проектом
# Извлеките из index.html его содержимое при помощи bs4 и парсера 'lxml'
# Вставьте содержимое в поле ответа

from zipfile import ZipFile
from bs4 import BeautifulSoup

with ZipFile('index.zip') as zip_file:
    with zip_file.open('index.html', 'r') as file:
        html_code = file.read().decode('utf-8')
        soup = BeautifulSoup(html_code, 'lxml')
        print(soup)