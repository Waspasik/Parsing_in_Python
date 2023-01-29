# Задача:

# Открыть сайт (https://parsinger.ru/selenium/1/1.html) с помощью selenium;
# Заполнить все существующие поля;
# Нажмите на кнопку;
# Скопируйте результат который появится рядом с кнопкой в случае если вы уложились в 5 секунд.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/selenium/1/1.html'
counter = 0
user_data = ['Patrick', 'Bateman', 'Psyco', '27', 'New York', 'bateman@psyco.com']

with webdriver.Chrome() as browser:
    browser.get(url)
    input_fields = browser.find_elements(By.CLASS_NAME, 'form')
    button = browser.find_element(By.ID, 'btn')
    for field in input_fields:
        field.send_keys(user_data[counter])
        counter += 1
        time.sleep(0.5)
    button.click()



# Задача:

# Откройте сайт (https://parsinger.ru/selenium/2/2.html);
# Применяем метод By.PARTIAL_LINK_TEXT или By.LINK_TEXT;
# Кликаем по ссылке с текстом 16243162441624;
# Результат будет ждать вас в теге <p id="result"></p>.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/selenium/2/2.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    search_text = browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624').click()
    time.sleep(1)
    get_result = browser.find_element(By.ID, 'result')
    print(get_result.text)



# Задача:

# Откройте сайт (https://parsinger.ru/selenium/3/3.html);
# Извлеките данные из каждого второго тега <p>;
# Сложите все значения, их всего 100 шт.

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/selenium/3/3.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    find_all_p = browser.find_elements(By.XPATH, "//div[@class='text']/p")
    print(sum(map(lambda p: int(p.text), find_all_p)))



# Задача:

# Откройте сайт (https://parsinger.ru/selenium/3/3.html);
# Извлеките данные из каждого второго тега <p>;
# Сложите все значения, их всего 100 шт.

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/selenium/3/3.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    find_all_p = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    print(sum(map(lambda p: int(p.text), find_all_p)))



# Задача:

# Откройте сайт (https://parsinger.ru/selenium/4/4.html);
# Установите все чек боксы в положение checked при помощи selenium и метода click();
# Когда все чек боксы станут активны, нажмите на кнопку;
# Результат появится в <p id="result">Result</p>.

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/selenium/4/4.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    all_checkboxes = browser.find_elements(By.CLASS_NAME, 'check')
    button = browser.find_element(By.CLASS_NAME, 'btn')
    for checkbox in all_checkboxes:
        checkbox.click()
    button.click()
    get_result = browser.find_element(By.ID, 'result')
    print(get_result.text)



# Задача:

# Откройте сайт;
# Установите чек боксы в положение checked при помощи selenium и метода click();
# Должны быть установлены те чек боксы, значение value="" которых, есть в списке numbers;
# Когда все необходимые чек боксы станут checked, кнопка станет активной, нажмите на неё и скопируйте результат;
# Результат появится в <p id="result">Result</p>.

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/selenium/5/5.html'
numbers = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38, 
39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73, 
74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118, 
119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153, 
154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207, 
208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233, 
234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255, 
256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314, 
318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349, 
353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412, 
419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451, 
452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479, 
480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519]

with webdriver.Chrome() as browser:
    browser.get(url)
    all_checkboxes = browser.find_elements(By.CLASS_NAME, 'check')
    button = browser.find_element(By.CLASS_NAME, 'btn')
    for checkbox in all_checkboxes:
        if int(checkbox.get_attribute('value')) in numbers:
            checkbox.click()
    button.click()
    get_result = browser.find_element(By.ID, 'result')
    print(get_result.text)



# Задача:

# Открываем сайт (https://parsinger.ru/selenium/7/7.html) с помощью selenium;
# Получаем значения всех элементов выпадающего списка;
# Суммируем(плюсуем) все значения;
# Вставляем получившийся результат в поле на сайте;
# Нажимаем кнопку и копируем длинное число.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/selenium/7/7.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    options = browser.find_elements(By.TAG_NAME, 'option')
    button = browser.find_element(By.CLASS_NAME, 'btn')
    input_field = browser.find_element(By.ID, 'input_result')
    input_field.send_keys(sum(map(lambda x: int(x.text), options)))
    time.sleep(1)
    button.click()
    time.sleep(1)
    print(browser.find_element(By.ID, 'result').text)



# Задача:

# Откройте сайт (https://parsinger.ru/selenium/6/6.html) при помощи selenium;
# Найдите значение выражения на странице;
# Найдите и выберите в выпадающем списке элемент с числом, которое у вас получилось после нахождения значения уравнения;
# Нажмите на кнопку и копируйте число.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/selenium/6/6.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    equation = browser.find_element(By.ID, 'text_box')
    options = browser.find_elements(By.TAG_NAME, 'option')
    button = browser.find_element(By.CLASS_NAME, 'btn')
    result_equation = eval(equation.text)
    time.sleep(1)
    browser.find_element(By.ID, 'selectId').click()
    time.sleep(1)
    for option in browser.find_elements(By.TAG_NAME, 'option'):
        if int(option.text) == result_equation:
            option.click()
            time.sleep(1)
    button.click()
    time.sleep(1)
    print(browser.find_element(By.ID, 'result').text)