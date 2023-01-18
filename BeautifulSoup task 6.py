# Задача:

# Открываем сайт https://parsinger.ru/html/index1_page_1.html
# Проходимся по всем категориям, страницам и карточкам с товарами(всего 160шт)
# Собираем с каждой карточки стоимость товара умножая на количество товара в наличии
# Складываем получившийся результат
# Получившуюся цифру с общей стоимостью всех товаров вставляем в поле ответа.

from bs4 import BeautifulSoup
from re import findall
import requests


def get_pagenation(category):
    response = requests.get(url_head + category)
    soup = BeautifulSoup(response.text, 'lxml')
    pagenation = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
    print(pagenation)
    get_goods_links(pagenation)


def get_goods_links(pagenation):
    for link in pagenation:
        response = requests.get(f'https://parsinger.ru/html/{link}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        link = soup.find_all('a', class_='name_item')
        goods_links = [url_head + item['href'] for item in soup.find_all('a', class_='name_item')]
        get_cost_goods(goods_links)


def get_cost_goods(goods_links):
    global total_cost
    for link in goods_links:
        response = requests.get(link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find('span', id='price').text
        count = soup.find('span', id='in_stock').text
        total_cost += int(findall(r'\d+', price)[0]) * int(findall(r'\d+', count)[0])


total_cost = 0
response = requests.get('https://parsinger.ru/html/index1_page_1.html')
soup = BeautifulSoup(response.text, 'lxml')
url_head = 'https://parsinger.ru/html/'
categories = [link['href'] for link in soup.find('div', class_='nav_menu').find_all('a')]
for category in categories:
    get_pagenation(category)

print(total_cost)