# Задача:

# Напишите код, который собирает данные со всех страниц и категорий на сайте
# https://parsinger.ru/html/index1_page_1.html и сохраните всё в таблицу используя
# библиотеку csv.

# Заголовки: указыать не нужно.

import csv
import requests
from bs4 import BeautifulSoup


def start_parsing():
    response = requests.get('https://parsinger.ru/html/index1_page_1.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    categories = [link['href'] for link in soup.find('div', class_='nav_menu').find_all('a')]
    for category in categories:
        get_pagenation(category)


def get_pagenation(category):
    response = requests.get(url_head + category)
    soup = BeautifulSoup(response.text, 'lxml')
    pagenation = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
    create_main_description(pagenation)


def create_main_description(pagenation):
    for link in pagenation:
        response = requests.get(url_head + link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        price = [x.text for x in soup.find_all('p', class_='price')]
        write_row_in_file(name, create_other_description(soup), price)


def create_other_description(soup):
    result = []
    for x in soup.find_all('div', class_='description'):
        full_description = x.text.strip().split('\n')
        description = [desc.split(':')[1].strip() for desc in full_description]
        description[1] = ' '+description[1]
        result.append(description)
    return result
  

def write_row_in_file(name, description, price):        
    with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for item_name, desc, item_price in zip(name, description, price):
            new_row = item_name, *desc, item_price
            writer.writerow(new_row)


with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
url_head = 'https://parsinger.ru/html/'
start_parsing()