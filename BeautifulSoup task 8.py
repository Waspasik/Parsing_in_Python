# Задача:

# Напишите код, который собирает данные в категории HDD со всех 4х страниц и сохраняет
# всё в таблицу используя библиотеку csv

# Заголовки :  Наименование, Бренд, Форм-фактор, Ёмкость, Объём буф. памяти, Цена

import csv
import requests
from bs4 import BeautifulSoup


def start_parsing():
    response = requests.get('https://parsinger.ru/html/index1_page_1.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    link_HDD = [link['href'] for link in soup.find('div', class_='nav_menu').find_all('a') if link.text == 'HDD'][0]
    get_pagenation(link_HDD)


def get_pagenation(category):
    response = requests.get(url_head + category)
    soup = BeautifulSoup(response.text, 'lxml')
    pagenation = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
    get_goods_links(pagenation)


def get_goods_links(pagenation):
    for link in pagenation:
        response = requests.get(url_head + link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        price = [x.text for x in soup.find_all('p', class_='price')]
        write_row_in_file(name, create_description(soup), price)


def create_description(soup):
    result = []
    for x in soup.find_all('div', class_='description'):
        full_description = x.text.strip().split('\n')
        print(full_description)
        print()
        description = [desc.split(':')[1].strip() for desc in full_description]
        description[1] = ' '+description[1]
        result.append(description)
    return result
  

def write_row_in_file(name, description, price):        
    with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        print(description)
        print(name)
        for item_name, desc, item_price in zip(name, description, price):
            new_row = item_name, *desc, item_price
            writer.writerow(new_row)


with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объём буф. памяти', 'Цена'])
url_head = 'https://parsinger.ru/html/'
start_parsing()