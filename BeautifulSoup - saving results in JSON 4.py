# Задача:

# Соберите данные со всех 5 категорий на сайте тренажере (https://parsinger.ru/html/index1_page_1.html)
# и соберите все данные с карточек + ссылка на карточку с товаром.

# По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела.
# Ключи в блоке description должны быть получены автоматически из атрибутов HTML элементов.

import json
import requests
from bs4 import BeautifulSoup


# Получаем ссылки каждой имеющейся страницы в категории и ссылки на товары.
# Присваиваем ключам значения с описаниями товара в соответствии с условием задачи.
def create_description(link, category):
    description_dict = {}
    response = requests.get(url_head + link)
    soup = BeautifulSoup(response.text, 'lxml')
    pagenation = [a['href'] for a in soup.find('div', class_='pagen').find_all('a')]

    # Получаем ссылки товаров с каждой страницы выбранной категории
    for link in pagenation:
        response = requests.get(url_head + link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        goods_links = [url_head + a['href'] for a in soup.find_all('a', class_='name_item')]

        # Создаем ключи и значения для словаря и добавляем словарь в итоговый список, очищаем словарь
        for link in goods_links:
            response = requests.get(link)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            description_dict['categories'] = category
            description_dict['name'] = soup.find('p', id='p_header').text
            description_dict['article'] = int(soup.find('p', class_='article').text.split(': ')[1])
            description_dict['description'] = dict([[li['id'], li.text.split(':')[1].strip()] for li in soup.find_all('li')])
            description_dict['count'] = int(soup.find('span', id='in_stock').text.split(': ')[1])
            description_dict['price'] = soup.find('span', id='price').text
            description_dict['old_price'] = soup.find('span', id='old_price').text
            description_dict['link'] = link
            result_json.append(description_dict)
            description_dict = {}


result_json = []
url_head = 'https://parsinger.ru/html/'
response = requests.get('https://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# Создаем список кортежей с ссылкой на категорию и наименованием категории,
# чтобы после передать наименование категории в словарь с описанием
categories = [(a['href'], a.find('div')['id']) for a in soup.find('div', class_='nav_menu').find_all('a')]     
for link_category, category in categories:
    create_description(link_category, category)


# Запись данных в формат JSON
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)