# Задача:

# Открываем сайт https://parsinger.ru/html/index3_page_4.html
# Проходимся по всем страницам в категории мыши (всего  4 страницы)
# На каждой странице посещаем каждую карточку с товаром (всего 32 товаров)
# В каждой карточке извлекаем при помощи bs4 артикул <p class="article"> Артикул: 80244813 </p>
# Складываем(плюсуем) все собранные значения
# Вставляем получившийся результат в поле ответа

from bs4 import BeautifulSoup
from re import findall
import requests


all_link = []
total = 0
response = requests.get('https://parsinger.ru/html/index3_page_4.html')
soup = BeautifulSoup(response.text, 'lxml')
main_link = 'https://parsinger.ru/html/'
page_counter = [int(link.text) for link in soup.find('div', class_='pagen').find_all('a')][-1]

for i in range(1, page_counter+1):
    response = requests.get(f'https://parsinger.ru/html/index3_page_{i}.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    link = soup.find_all('a', class_='name_item')
    for x in link:
        all_link.append(main_link + x['href'])

for link in all_link:
    response = requests.get(link)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    article = soup.find('p', class_='article').text
    total += int(findall(r'\d+', article)[0])

print(total)