# Задача:

# Откройте сайт (https://parsinger.ru/asyncio/create_soup/1/index.html), там есть 501 ссылка,
# секретный код лежит только на четырёх из них;
# Напишите асинхронный код, который найдёт все четыре кода и суммирует их;
# Суммируйте все полученный значеия.

import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup
from aiohttp_retry import RetryClient, ExponentialRetry


links = []
total = 0
domain = 'https://parsinger.ru/asyncio/create_soup/1/'


def get_soup(url):
    response = requests.get(url=url)
    return BeautifulSoup(response.text, 'lxml')


def get_urls(soup):
    all_links = soup.find('div', class_='item_card').find_all('a')
    for link in all_links:
        links.append(domain + link['href'])


async def get_data(session, link):
    retry_options = ExponentialRetry(attempts=5)
    retry_client = RetryClient(raise_for_status=False, retry_options=retry_options, client_session=session,
                               start_timeout=0.5)
    async with retry_client.get(link) as response:
        #print(response.status)
        if response.ok:
            resp = await response.text()
            soup = BeautifulSoup(resp, 'lxml')
            global total
            total += int(soup.find('p', class_='text').text)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in links:
            task = asyncio.create_task(get_data(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)


url = 'https://parsinger.ru/asyncio/create_soup/1/index.html'
soup = get_soup(url)
get_urls(soup)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
print(total)