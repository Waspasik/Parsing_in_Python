# Задача:

# На сайте https://parsinger.ru/table/1/index.html расположена таблица;
# Цель: Собрать все уникальные числа из таблицы (кроме цифр в заголовке) и суммировать их;
# Полученный результат вставить в поле ответа.

from bs4 import BeautifulSoup
import requests


numbers = set()
response = requests.get('https://parsinger.ru/table/1/index.html')
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find('table').find_all('tr')
for row in table[1::]:
    for num in row.text.split():
        numbers.add(float(num))

print(sum(numbers))



# Задача:

# На сайте https://parsinger.ru/table/2/index.html расположена таблица;
# Цель: Собрать числа с 1го столбца и суммировать их;
# Полученный результат вставить в поле ответа.

from bs4 import BeautifulSoup
import requests


response = requests.get('https://parsinger.ru/table/2/index.html')
soup = BeautifulSoup(response.text, 'lxml')
print(sum(float(row.text.split()[0]) for row in soup.find('table').find_all('tr')[1::]))



# Задача:

# На сайте https://parsinger.ru/table/3/index.html расположена таблица;
# Цель: Собрать числа которые выделены жирным шрифтом и суммировать их;
# Полученный результат вставить в поле ответа.

from bs4 import BeautifulSoup
import requests


response = requests.get('https://parsinger.ru/table/3/index.html')
soup = BeautifulSoup(response.text, 'lxml')
print(sum(float(num.text) for num in soup.find_all('b')))



# # Задача:

# На сайте https://parsinger.ru/table/4/index.html расположена таблица;
# Цель: Собрать числа в зелёных ячейках и суммировать их;
# Полученный результат вставить в поле ответа.

from bs4 import BeautifulSoup
import requests


response = requests.get('https://parsinger.ru/table/4/index.html')
soup = BeautifulSoup(response.text, 'lxml')
print(sum(float(num.text) for num in soup.find_all('td', class_='green')))



# Задача:

# На сайте https://parsinger.ru/table/5/index.html расположена таблица;
# Цель: Умножить число в оранжевой ячейке на число в голубой ячейке в той же строке и всё суммировать;
# Полученный результат вставить в поле ответа.

from bs4 import BeautifulSoup
import requests


total = []
response = requests.get('https://parsinger.ru/table/5/index.html')
soup = BeautifulSoup(response.text, 'lxml')
for row in soup.find_all('tr'):
    for num in row.find_all('td', class_='orange'):
        total.append(float(num.text) * int(row.text.split()[-1]))
print(sum(total))



# Задача:

# На сайте https://parsinger.ru/table/5/index.html расположена таблица;
# Цель: Написать скрипт который формирует словарь, где ключ будет автоматически формироваться из
# заголовка столбцов, а значения это сумма всех чисел в столбце;
# Округлить каждое число в значении до 3х символов после запятой.
# Полученный словарь вставить в поле ответа.

from bs4 import BeautifulSoup
import requests


table = {}
response = requests.get('https://parsinger.ru/table/5/index.html')
soup = BeautifulSoup(response.text, 'lxml')
headers = [row.text for row in soup.find_all('th')]
for i in range(len(headers)):
    table[f'{i+1} column'] = round(sum(float(row.text.split()[i]) for row in soup.find_all('tr')[1::]), 3)
print(table)