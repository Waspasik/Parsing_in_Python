# Задача:

# Откройте сайт (https://parsinger.ru/expectations/3/index.html) при помощи Selenium;
# На сайте есть кнопка, которая становится активной после загрузки страницы с рандомной задержкой, от 1 до 3 сек;
# После нажатия на кнопку, в title начнут появляться коды, с рандомным временем, от 0.1 до 0.6 сек;
# Ваша задача успеть скопировать код из id="result", когда  title будет равен "345FDG3245SFD".

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/3/index.html')
    while True:
        WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
        if WebDriverWait(browser, 40).until(EC.title_is('345FDG3245SFD')):
            print(browser.find_element(By.ID, 'result').text)
            break



# Задача:

# Откройте сайт (https://parsinger.ru/expectations/4/index.html) при помощи Selenium;
# На сайте есть кнопка, которая становится активной после загрузки страницы с рандомной задержкой, от 1 до 3 сек;
# После нажатия на кнопку, в title начнут появляться коды, с рандомным временем, от 0,1 до 0.6 сек;
# В этот раз второй раз на кнопку кликать не нужно, а нужно получить title целиком, если title содержит "JK8HQ"
# Используйте метод title_contains(title) с прошлого урока.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/4/index.html')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    while True:
        if WebDriverWait(browser, 100).until(EC.title_contains('JK8HQ')):
            print(browser.execute_script("return document.title;"))
            break



# Задача:

# Откройте сайт (https://parsinger.ru/expectations/5/index.html) при помощи Selenium;
# На сайте есть кнопка, поведение которой вам знакомо;
# После нажатие на кнопку, на странице начнётся создание элементов class с рандомными значениями;
# Ваша задача применить метод, чтобы он вернул содержимое элемента с классом "BMH21YY", когда он появится на странице.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/5/index.html')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    while True:
        if WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY'))):
            print(browser.find_element(By.CLASS_NAME, 'BMH21YY').text)
            break