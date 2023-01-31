# Задача:

# Откройте сайт (https://parsinger.ru/scroll/4/index.html) с помощью Selenium;
# На сайте есть 50 кнопок, которые визуально перекрыты блоками;
# После нажатия на кнопку в id="result" появляется уникальное для каждой кнопки число;
# Цель: написать скрипт, который нажимает поочерёдно все кнопки и собирает уникальные числа.

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/scroll/4/index.html'
result = 0

with webdriver.Chrome() as browser:
    browser.get(url)
    buttons = browser.find_elements(By.CLASS_NAME, 'btn')
    for button in buttons:
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        result += int(browser.find_element(By.ID, 'result').text)

print(result)