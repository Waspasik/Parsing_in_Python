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