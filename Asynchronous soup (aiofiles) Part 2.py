# Глубина парсинга уровень 2

# Откройте сайт (https://parsinger.ru/asyncio/aiofile/3/index.html), на нём есть 100 ссылок,
# в каждой из них есть ещё 10 ссылок, в каждой из 10 ссылокесть 8-10 изображений, структура
# как на картинке ниже;
# Ваша задача: Написать асинхронный код который скачает все уникальные изображения которые
# там есть (они повторяются, в это задании вам придётся скачать 2615 изображений).

import time
import aiofiles
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os


def get_folder_size(filepath, size=0):
    for root, _, files in os.walk(filepath):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size


async def write_file(session, url, img_name):
    async with aiofiles.open(f'images/{img_name}', mode='wb') as file:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(512):
                await file.write(x)
        print(f'Изображение {img_name} сохранено')


async def main():
    schema = 'https://parsinger.ru/asyncio/aiofile/3/'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            main_soup = BeautifulSoup(await response.text(), 'lxml')
            links = [schema + a['href'] for a in main_soup.find_all('a')]
            image_links = []
            for link in links:
                schema2 = 'https://parsinger.ru/asyncio/aiofile/3/depth2/'
                async with session.get(link) as response2:
                    soup = BeautifulSoup(await response2.text(), 'lxml')
                    links = [schema2 + a['href'] for a in soup.find_all('a')]
                    for link in links:
                        async with session.get(link) as response3:
                            soup = BeautifulSoup(await response3.text(), 'lxml')
                            [image_links.append(img['src'])
                             for img in soup.find_all('img')]
            tasks = []
            for link in set(image_links):
                img_name = link.split('/')[-1]
                task = asyncio.create_task(write_file(session, link, img_name))
                tasks.append(task)
            await asyncio.gather(*tasks)


url = 'https://parsinger.ru/asyncio/aiofile/3/index.html'

start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

print(
    f'Cохранено изображений {len(os.listdir("images/"))} за {round(time.perf_counter() - start, 3)} сек')
print(get_folder_size('D:/Python/Parsing/images'))
