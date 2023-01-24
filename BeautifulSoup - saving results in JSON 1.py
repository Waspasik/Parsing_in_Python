# Задача:

# Выберите 1 любую категорию на сайте тренажере (https://parsinger.ru/html/index5_page_1.html)
# и соберите все данные с карточек (была выбрана категория наушников).

# По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела.

import json
import requests
from bs4 import BeautifulSoup


# Запускаем цепочку функций по парсингу начиная с нахождения ссылки нужного раздела
def start_parsing():
    response = requests.get('https://parsinger.ru/html/index1_page_1.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    link_headphones = [link['href'] for link in soup.find('div', class_='nav_menu').find_all('a') if link.text == 'НАУШНИКИ'][0]
    get_pagenation(link_headphones)


# Получаем ссылки каждой имеющейся страницы в разделе
def get_pagenation(link):
    response = requests.get(url_head + link)
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


# Добавляем словарь с описанием в список, который будет передан в метод .dump() для записи данных в формате JSON
def create_list_for_json(name, item_description, price):
    for item_name, item_desc, item_price in zip(name, item_description, price):
        result_json.append({
            'name': item_name,
            'brand': item_desc[0].split(':')[1].strip(),
            'connection type': item_desc[1].split(':')[1].strip(),
            'color': item_desc[2].split(':')[1].strip(),
            'headphone type': item_desc[3].split(':')[1].strip(),
            'price': item_price
    })


result_json = []
url_head = 'https://parsinger.ru/html/'
start_parsing()

# Запись данных в формат JSON
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)