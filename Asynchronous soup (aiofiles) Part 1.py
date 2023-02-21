# Глубина парсинга уровень 1

# Откройте сайт (https://parsinger.ru/asyncio/aiofile/2/index.html), на нём есть 50 ссылок, в каждой
# ссылке лежит по 10 изображений;
# Ваша задача: Написать асинхронный код который скачает все уникальные изображения которые там есть
# (они повторяются, а уникальных всего 449);
# Вставьте размер всех скачанных изображений в поле для ответа;
# Асинхронный код должен обработать все ссылки и скачать все изображения примерно за 20-30 сек,
# скорость зависит от скорости вашего интернет соединения.

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
            async for x in response.content.iter_chunked(1024):
                await file.write(x)
        print(f'Изображение {img_name} сохранено')


async def main():
    schema = 'https://parsinger.ru/asyncio/aiofile/2/'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            main_soup = BeautifulSoup(await response.text(), 'lxml')
            links = [schema + a['href'] for a in main_soup.find_all('a')]

            for link in links:
                async with session.get(link) as response2:
                    soup = BeautifulSoup(await response2.text(), 'lxml')
                    [image_links.append(f'{img["src"]}')
                     for img in soup.find_all('img')
                     if f'{img["src"]}' not in image_links]

            tasks = []

            for link in image_links:
                img_name = link.split('/')[-1]
                task = asyncio.create_task(write_file(session, link, img_name))
                tasks.append(task)

            await asyncio.gather(*tasks)


url = 'https://parsinger.ru/asyncio/aiofile/2/index.html'
image_links = []

start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

print(
    f'Cохранено изображений {len(os.listdir("images/"))} за {round(time.perf_counter() - start, 3)} сек')
print(get_folder_size('D:/Python/Parsing/images'))
