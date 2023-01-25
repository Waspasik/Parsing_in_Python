# Задача:

# Соберите данные со всех 5 категорий на сайте тренажере (https://parsinger.ru/html/index1_page_1.html)
# и соберите все данные с карточек.

# По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела.

import json
import requests
from bs4 import BeautifulSoup


# Запускаем цепочку функций по парсингу начиная с нахождения ссылок имеющихся категорий товаров
def start_parsing():
    response = requests.get('https://parsinger.ru/html/index1_page_1.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    categories = [link['href'] for link in soup.find('div', class_='nav_menu').find_all('a')]
    for category in categories:
        get_pagenation(category)


# Получаем ссылки каждой имеющейся страницы в отдельной категории
def get_pagenation(category):
    response = requests.get(url_head + category)
    soup = BeautifulSoup(response.text, 'lxml')
    pagenation = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
    create_description(pagenation)


# Создаем переменные с описаниями в соответствии с поставленным условием задачи
def create_description(pagen):
    for link in pagen:
        response = requests.get(url_head + link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        item_description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
        price = [x.text for x in soup.find_all('p', class_='price')]
        create_list_for_json(name, item_description, price)


# Добавляем словарь с описанием в итоговый список
def create_list_for_json(name, item_description, price):
    for item_name, item_desc, item_price in zip(name, item_description, price):
        result_json.append({
            'Наименование': item_name,
            item_desc[0].split(':')[0].strip(): item_desc[0].split(':')[1].strip(),
            item_desc[1].split(':')[0].strip(): item_desc[1].split(':')[1].strip(),
            item_desc[2].split(':')[0].strip(): item_desc[2].split(':')[1].strip(),
            item_desc[3].split(':')[0].strip(): item_desc[3].split(':')[1].strip(),
            'Цена': item_price
    })
    

result_json = []
url_head = 'https://parsinger.ru/html/'
start_parsing()

# Запись данных в формат JSON из итогового списка
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)