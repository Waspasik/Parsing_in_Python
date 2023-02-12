# Задача:

# Откройте сайт (https://parsinger.ru/blank/modal/2/index.html) при помощи Selenium;
# На сайте есть 100 buttons;
# При нажатии на одну из кнопок в  теге <p id="result">Code</p> появится код.

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/blank/modal/2/index.html')
    for button in browser.find_elements(By.CLASS_NAME, 'buttons'):
        button.click()
        browser.switch_to.alert.accept()
        secret_code = browser.find_element(By.ID, 'result').text
        if secret_code:
            print(secret_code)
            break



# Задача:

# Откройте сайт (https://parsinger.ru/blank/modal/3/index.html) при помощи Selenium;
# На сайте есть 100 buttons;
# При нажатии на любую кнопку появляется confirm с пин-кодом;
# Текстовое поле под кнопками проверяет правильность пин-кода;
# Ваша задача, найти правильный пин-код и получить секретный код.


from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/blank/modal/3/index.html')
    for button in browser.find_elements(By.CLASS_NAME, 'buttons'):
        button.click()
        confirm = browser.switch_to.alert
        pin_code = confirm.text
        confirm.accept()
        browser.find_element(By.ID, 'input').send_keys(pin_code)
        browser.find_element(By.ID, 'check').click()
        secret_code = browser.find_element(By.ID, 'result').text
        if secret_code != 'Неверный пин-код':
            print(secret_code)
            break



# Задача:

# Откройте сайт (https://parsinger.ru/blank/modal/4/index.html) при помощи Selenium;
# На сайте есть список пин-кодов и только один правильный;
# Для проверки пин-кода используйте кнопку "Проверить"
# Ваша задача, найти правильный пин-код и получить секретный код.

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/blank/modal/4/index.html')
    for pin in map(lambda pin: pin.text, browser.find_elements(By.CLASS_NAME, 'pin')):
        browser.find_element(By.ID, 'check').click()
        prompt = browser.switch_to.alert
        prompt.send_keys(pin)
        prompt.accept()
        result = browser.find_element(By.ID, 'result').text
        if result.isdigit():
            print(result)
            break


            
# Задача:

# Откройте сайт (https://parsinger.ru/window_size/1/) с помощью selenium;
# Необходимо открыть окно таким размером, чтобы рабочая область страницы составляла 555px на 555px;
# Учитывайте размеры границ браузера;
# Результат появится в id="result".

from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/1/index.html')
    browser.set_window_size(568, 686)
    print(browser.find_element(By.ID, 'result').text)

    
    
# Задача:

# Откройте сайт (https://parsinger.ru/blank/3/index.html) с помощью Selenium;
# На сайте есть 10 buttons, каждый button откроет сайт в новой вкладке;
# Каждая вкладка имеет в title уникальное число;
# Цель - собрать числа с каждой вкладки и суммировать их.

from selenium import webdriver
from selenium.webdriver.common.by import By


total = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/blank/3/index.html')
    for button in browser.find_elements(By.CLASS_NAME, 'buttons'):
        button.click()
    for tab in browser.window_handles:
        browser.switch_to.window(tab)
        if browser.execute_script("return document.title;").isdigit():
            total += int(browser.execute_script("return document.title;"))
    print(total)



# Задача:

# У вас есть список сайтов, 6 шт;
# На каждом сайте есть chekbox, нажав на этот chekbox появится код;
# Ваша задача написать скрипт, который открывает при помощи Selenium все сайты во вкладках (.window_handles);
# Проходит в цикле по каждой вкладке, нажимает на chekbox и сохранеят код;
# Из каждого числа, необходимо извлечь корень, функцией sqrt();
# Суммировать получившиеся корни и вставить результат в поле для ответа.

from math import sqrt
from selenium import webdriver
from selenium.webdriver.common.by import By


numbers = []
sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html', 'http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]
new_tab = 'window.open("{}", "_blank{}");'

with webdriver.Chrome() as browser:
    for index, url in enumerate(sites):
        if not index:
            browser.get(url)
        else:
            browser.execute_script(new_tab.format(url, index))

    for window in browser.window_handles:
        browser.switch_to.window(window)
        browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
        numbers.append(int(browser.find_element(By.ID, 'result').text))

    total = sum(map(lambda num: sqrt(num), numbers))
    print(round(total, 9))
