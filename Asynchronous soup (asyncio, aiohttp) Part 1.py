# Задача:

# Откройте сайт тренажёр (https://parsinger.ru/html/index1_page_1.html);
# Напишите асинхронный код, который обработает все карточки(160шт);
# Необходимо вычислить общий размер скидки для всех товаров в рублях.

import aiohttp
import asyncio
import requests
from re import findall
from bs4 import BeautifulSoup
from aiohttp_retry import RetryClient, ExponentialRetry


categories = []
pagenation = []
total_discount = 0
domain = 'https://parsinger.ru/html/'


def get_soup(url):
    response = requests.get(url=url)
    return BeautifulSoup(response.text, 'lxml')


def get_urls_categories(soup):
    all_link = soup.find('div', class_='nav_menu').find_all('a')

    for cat in all_link:
        categories.append(domain + cat['href'])


def get_urls_pages(categories):
    for category in categories:
        resp = requests.get(url=category)
        soup = BeautifulSoup(resp.text, 'lxml')
        for pagen in soup.find('div', class_='pagen').find_all('a'):
            pagenation.append(domain + pagen['href'])


async def get_data(session, link):
    retry_options = ExponentialRetry(attempts=5)
    retry_client = RetryClient(raise_for_status=False, retry_options=retry_options, client_session=session,
                               start_timeout=0.5)
    async with retry_client.get(link) as response:
        if response.ok:
            resp = await response.text()
            soup = BeautifulSoup(resp, 'lxml')
            item_card = [a['href'] for a in soup.find_all('a', class_='name_item')]
            for x in item_card:
                url2 = domain + x
                async with session.get(url=url2) as response2:
                    resp2 = await response2.text()
                    soup2 = BeautifulSoup(resp2, 'lxml')
                    global total_discount
                    old_price = int(findall(r'\d+', soup2.find('span', id='old_price').text)[0])
                    price = int(findall(r'\d+', soup2.find('span', id='price').text)[0])
                    amount = int(soup2.find('span', id='in_stock').text.split(': ')[-1])
                    discount = (old_price - price) * amount
                    total_discount += discount


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in pagenation:
            task = asyncio.create_task(get_data(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)


url = 'https://parsinger.ru/html/index1_page_1.html'
soup = get_soup(url)
get_urls_categories(soup)
get_urls_pages(categories)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
print(total_discount)