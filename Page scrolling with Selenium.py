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



# Задача:

# Откройте сайт (https://parsinger.ru/scroll/2/index.html) с помощью Selenium;
# На сайте есть 100 чекбоксов, 25 из них вернут число;
# Ваша задача суммировать все появившиеся числа.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/2/index.html')
    
    for input in browser.find_elements(By.TAG_NAME, 'input'):
        ActionChains(browser).move_to_element(input).click().perform()
    
    print(sum(int(span.text) for span in browser.find_elements(By.TAG_NAME, 'span') if span.text.isdigit()))



# Задача:

# Откройте сайт сайт (https://parsinger.ru/scroll/3/) с помощью Selenium;
# Ваша задача, получить числовое значение  id="число" с каждого тега <input> который при нажатии вернул число;
# Суммируйте все значения.

from re import findall
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/3/')
    
    for input in browser.find_elements(By.TAG_NAME, 'input'):
        ActionChains(browser).move_to_element(input).click().perform()
    
    print(sum(int(findall(r'\d+', span.get_attribute('id'))[0])
              for span in browser.find_elements(By.TAG_NAME, 'span')
              if span.text.isdigit()))
