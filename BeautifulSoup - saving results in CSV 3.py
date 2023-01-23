# Задача:

# Напишите код, который собирает данные в категории watch (https://parsinger.ru/html/index1_page_1.html)
# c каждой карточки, всего их 32.

# Обязательные Заголовки :  Наименование, Артикул, Бренд, Модель, Тип, Технология экрана, Материал корпуса,
# Материал браслета, Размер, Сайт производителя, Наличие, Цена, Старая цена,  Ссылка на карточку с товаром.

# Всего должно быть 14 заголовков.

import csv
import requests
from bs4 import BeautifulSoup


def start_parsing():
    response = requests.get('https://parsinger.ru/html/index1_page_1.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    link_HDD = [link['href'] for link in soup.find('div', class_='nav_menu').find_all('a') if link.text == 'ЧАСЫ'][0]
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
        goods_links = [url_head + item['href'] for item in soup.find_all('a', class_='name_item')]
        create_description(goods_links)
        

def create_description(links):
    for link in links:
        response = requests.get(link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = soup.find('p', id='p_header').text
        print(name)
        article = soup.find('p', class_='article').text.split(': ')[1]
        description = [desc.text.strip().split(': ')[1] for desc in soup.find('ul', id='description').find_all('li')]
        in_stock = soup.find('span', id='in_stock').text.split(': ')[1]
        price = soup.find('span', id='price').text
        old_price = soup.find('span', id='old_price').text
        link_product = link
        write_row_in_file(name, article, description, in_stock, price, old_price, link_product)
  

def write_row_in_file(name, article, description, in_stock, price, old_price, link_product):   
    with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        new_row = name, article, *description, in_stock, price, old_price, link_product
        writer.writerow(new_row)


with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана',
                     'Материал корпуса', 'Материал браслета', 'Размер', 'Сайт производителя', 
                     'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром'])
url_head = 'https://parsinger.ru/html/'
start_parsing()