# Задача:

# Открываем сайт https://parsinger.ru/html/index1_page_1.html
# Извлекаем при помощи bs4 данные о стоимости часов (всего 8 шт)
# Складываем все числа
# Вставляем результат в поле ответа 

from bs4 import BeautifulSoup
from re import findall
import requests

response = requests.get('https://parsinger.ru/html/index1_page_1.html').text
soup = BeautifulSoup(response, 'lxml')
div = ' '.join(item.text for item in soup.find_all('p', class_='price'))
total_price = sum(map(int, findall(r'\d+', div)))
print(total_price)