# Задача:

# Откройте сайт (https://parsinger.ru/methods/1/index.html) с помощью Selenium;
# При обновлении сайта, в id="result" появится число;
# Обновить страницу возможно придется много раз, т.к. число появляется не часто.

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/methods/1/index.html'
counter = 0

with webdriver.Chrome() as browser:
    browser.get(url)
    while True:
        browser.refresh()
        counter += 1
        except_result = browser.find_element(By.ID, 'result').text
        if except_result.isdigit():
            print(except_result, counter, sep='_')
            break



# Задача:

# Откройте сайт (https://parsinger.ru/methods/3/index.html) с помощью Selenium;
# На сайте есть определённое количество секретных cookie;
# Ваша задача получить все значения и суммировать их.

from selenium import webdriver


url = 'https://parsinger.ru/methods/3/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    print(sum(int(cookie['value'])
          for cookie in browser.get_cookies()
          if 'secret' in cookie['name']))



# Задача:

# Откройте сайт (https://parsinger.ru/methods/3/index.html) с помощью Selenium;
# Ваша задача получить все значения cookie с чётным числом после "_" и суммировать их.

from selenium import webdriver


url = 'https://parsinger.ru/methods/3/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    print(sum(int(cookie['value'])
          for cookie in browser.get_cookies()
          if int(cookie['name'].split('_')[-1]) % 2 == 0))



# Задача:

# Откройте сайт с помощью Selenium;
# На сайте есть 42 ссылки, у каждого сайта по ссылке есть cookie с определёнными сроком жизни;
# Цель: написать скрипт, который сможет найти среди всех ссылок страницу с самым длинным сроком
# жизни cookie и получить с этой страницы число.

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/methods/5/index.html'
max_expiry = 0
number = 0

with webdriver.Chrome() as browser:
    browser.get(url)
    links = browser.find_elements(By.CLASS_NAME, 'urls')
    for link in links:
        link.click()
        expiry = int(browser.get_cookies()[0]['expiry'])
        if expiry > max_expiry:
            max_expiry = expiry
            number = int(browser.find_element(By.ID, 'result').text)
        browser.back()

print(max_expiry, number)