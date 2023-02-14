# Задача:

# Откройте сайт c помощью Selenium;
# Напишите скрипт который перетащит красный блок из первого поля во второе;
# После перемещения блока, появится токен.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/1/index.html')
    source = browser.find_element(By.ID, 'draggable')
    target = browser.find_element(By.ID, 'field2')
    action = ActionChains(browser)
    action.drag_and_drop(source, target).release().perform()
    print(browser.find_element(By.ID, 'result').text)



# Задача:

# Откройте сайт (https://parsinger.ru/draganddrop/2/index.html) c помощью Selenium;
# На сайте есть четыре пронумерованных блока;
# Напишите скрипт который перетащит красный квадрат поочерёдно в каждый блок;
# После перемещения красного квадрата по всем блокам , появится токен.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/2/index.html')
    for box in browser.find_elements(By.CLASS_NAME, 'box'):
        source = browser.find_element(By.ID, 'draggable')
        action = ActionChains(browser)
        action.drag_and_drop(source, box).release().perform()
    print(browser.find_element(By.ID, 'message').text)



# Задача:

# Откройте сайт (https://parsinger.ru/draganddrop/3/index.html) c помощью Selenium;
# На сайте есть синий квадрат, который нужно перетащить по оси X;
# Напишите скрипт который перетащит синий квадрат поочерёдно через все красные точки;
# После перемещения синего квадрата по всем точкам, появится токен.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/3/index.html')
    source = browser.find_element(By.ID, 'block1')
    action = ActionChains(browser)
    for _ in range(5):
        action.click_and_hold(source).move_by_offset(50, 0).release().perform()
    time.sleep(3)
    print(browser.find_element(By.ID, 'message').text)