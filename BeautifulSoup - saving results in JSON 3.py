# Задача:

# Выберите 1 любую категорию на сайте тренажере (https://parsinger.ru/html/index1_page_1.html)
# и соберите все данные с карточек товаров + ссылка на карточку (была выбрана категория МЫШИ).

# По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела.
# Ключи в блоке description должны быть получены автоматически из атрибутов HTML элементов.

import json
import requests
from bs4 import BeautifulSoup


# Получаем ссылки каждой имеющейся страницы в категории и ссылки на товары.
# Создаем переменные с описаниями в соответствии с поставленным условием задачи.
def create_description(link_mouses, category):
    description_dict = {}
    response = requests.get(url_head + link_mouses)
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


# Находим ссылку на необходимую категорию
for a in soup.find('div', class_='nav_menu').find_all('a'):
    if a.find('div')['id'] == 'mouse':
        name_of_category = a.find('div')['id']
        link_mouses = a['href']
        create_description(link_mouses, name_of_category)


# Запись данных в формат JSON
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)