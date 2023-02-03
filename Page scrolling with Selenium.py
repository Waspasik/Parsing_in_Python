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

    
    
# Задача:

# Откройте сайт (https://parsinger.ru/infiniti_scroll_1/) с помощью Selenium;
# На сайте есть список из 100 элементов, которые генерируются при скроллинге;
# В списке есть интерактивные элементы, по которым можно осуществить скроллинг вниз;
# Цель: получить все значение в элементах, сложить их.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


spans_list = []
total = 0
flag = True

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')

    while flag:
        tags_span = [span for span in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span')]
        for span in tags_span:
            if span not in spans_list:
                spans_list.append(span)
                print(span.text)
                total += int(span.text)
                ActionChains(browser).move_to_element(span).perform()
            if span.get_attribute('class') == 'last-of-list':
                flag = False
    
    print(total)



# Задача:

# Откройте сайт (https://parsinger.ru/infiniti_scroll_2/) с помощью Selenium;
# На сайте есть список из 100 элементов, которые генерируются при скроллинге;
# В списке есть интерактивные элементы, по которым можно осуществить скроллинг вниз;
# Используйте Keys.DOWN или .move_to_element();
# Цель: получить все значение в элементах, сложить их.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


tags_list = []
total = 0
flag = True

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')

    while flag:
        p_tags = [p for p in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'p')]
        for p in p_tags:
            if p not in tags_list:
                tags_list.append(p)
                total += int(span.text)
                ActionChains(browser).move_to_element(div).scroll_by_amount(1, 20).perform()
            if span.get_attribute('class') == 'last-of-list':
                flag = False
    
    print(total)

    
    
# Задача:

# Откройте сайт (https://parsinger.ru/infiniti_scroll_3/) с помощью Selenium 
# На сайте есть 5 окошек с подгружаемыми элементами, в каждом по 100 элементов;
# Необходимо прокрутить все окна в самый низ;
# Цель: получить все значение в каждом из окошек и сложить их.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


total = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')
    for i in range(1, 6):
        div = browser.find_element(By.XPATH, f'//*[@id="scroll-container_{i}"]/div')
        flag = True
        tags_list = []

        while flag:
            span_tags = [span for span in browser.find_element(By.ID, f'scroll-container_{i}').find_elements(By.TAG_NAME, 'span')]
            for span in span_tags:
                if span not in tags_list:
                    tags_list.append(span)
                    total += int(span.text)
                    ActionChains(browser).move_to_element(div).scroll_by_amount(1, 20).perform()
                if span.get_attribute('class') == 'last-of-list':
                    flag = False
    
    print(total)
