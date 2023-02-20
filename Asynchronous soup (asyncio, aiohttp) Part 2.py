# Задача:

# Откройте сайт (https://parsinger.ru/asyncio/create_soup/1/index.html), там есть 501 ссылка,
# секретный код лежит только на четырёх из них;
# Напишите асинхронный код, который найдёт все четыре кода и суммирует их;
# Суммируйте все полученный значеия.

import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup


def get_urls():
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    shema = 'https://parsinger.ru/asyncio/create_soup/1/'
    all_links = soup.find('div', class_='item_card').find_all('a')
    for link in all_links:
        links.append(shema + link['href'])


async def main(link):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            if response.ok:
                resp = await response.text()
                soup = BeautifulSoup(resp, 'lxml')
                total.append(int(soup.find('p', class_='text').text))


url = 'https://parsinger.ru/asyncio/create_soup/1/index.html'
links, total = [], []
get_urls()

task = [main(link) for link in links]
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(asyncio.wait(task))
print(sum(total))
