# Задача:

# Откройте сайт https://parsinger.ru/html/index3_page_1.html
# Извлеките названия товара с каждой страницы (всего 4х страниц)
# Данные с каждой страницы должны хранится в списке.
# По итогу работы должны получится 4 списка которые хранятся в списке(список списков)
# Отправьте получившийся список списков в поле ответа.
# Метод strip()использовать не нужно

from bs4 import BeautifulSoup
import requests


result = []
response = requests.get('https://parsinger.ru/html/index3_page_1.html')
soup = BeautifulSoup(response.text, 'lxml')
main_page = 'http://parsinger.ru/html/'
pages = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

for page in pages:
    response = requests.get(main_page + page)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    item_names = [name.text for name in soup.find_all('a', class_='name_item')]
    result.append(item_names)
    
print(result)