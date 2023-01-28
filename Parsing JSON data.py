# Используйте полученный по ссылке (https://parsinger.ru/downloads/get_json/res.json) JSON,
# чтобы посчитать количество товара в каждой категории.

# На вход ожидается словарь {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N},
# где N - это общее количество товаров.

import requests


total_count = {}
url = 'https://parsinger.ru/downloads/get_json/res.json'
response = requests.get(url=url).json()
for item in response:
    total_count[item['categories']] = total_count.get(item['categories'], 0) + int(item['count'])

print(total_count)



# Используйте полученный по ссылке (https://parsinger.ru/downloads/get_json/res.json) JSON,
# чтобы посчитать стоимость товаров в каждой отдельной категории.

# На вход ожидается словарь {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N},
# где N - это общее количество товаров.

import requests
from re import findall


total_price = {}
url = 'https://parsinger.ru/downloads/get_json/res.json'
response = requests.get(url=url).json()
for item in response:
    total_price[item['categories']] = total_price.get(item['categories'], 0) + int(findall(r'\d+', item['price'])[0]) * int(item['count'])

print(total_price)