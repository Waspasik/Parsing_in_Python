# Задача:

# Открываем сайт https://parsinger.ru/html/hdd/4/4_1.html
# Получаем данные при помощи bs4 о старой цене и новой цене
# По формуле высчитываем процент скидки
# Формула (старая цена - новая цена) * 100 / старая цена)
# Вставьте получившийся результат в поле ответа
# Ответ должен быть числом с 1 знаком после запятой.

from bs4 import BeautifulSoup
from re import findall
import requests

response = requests.get('https://parsinger.ru/html/hdd/4/4_1.html').text
soup = BeautifulSoup(response, 'lxml')
new_price = int(soup.find('span', id='price').text.split()[0])
old_price = int(soup.find('span', id='old_price').text.split()[0])
discount = (old_price - new_price) * 100 / old_price
print(round(discount, 1))