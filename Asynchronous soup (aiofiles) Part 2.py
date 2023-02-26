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
from tqdm import tqdm
from aiohttp_retry import RetryClient, ExponentialRetry
import os


def get_folder_size(filepath, size=0):
    for root, _, files in os.walk(filepath):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size


async def download_image(session, url, img_name):
    async with aiofiles.open(f'images/{img_name}', mode='wb') as file:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(3072):
                await file.write(x)


async def find_images(session, url, pbar):
    retry_options = ExponentialRetry(attempts=5)
    retry_client = RetryClient(
        retry_options=retry_options, client_session=session, start_timeout=0.5)

    async with retry_client.get(url) as response:
        if response.ok:
            soup = BeautifulSoup(await response.text(), 'lxml')
            image_links = [img['src'] for img in soup.find_all('img') if img['src'] not in all_image_links]
            all_image_links.update([img['src'] for img in soup.find_all('img')])
            for link in image_links:
                img_name = link.split('/')[-1]
                await download_image(session, link, img_name)
                pbar.update(1)


async def get_links(session, url):
    retry_options = ExponentialRetry(attempts=5)
    retry_client = RetryClient(retry_options=retry_options, client_session=session, start_timeout=0.5)
    async with retry_client.get(url) as response:
        if response.ok:
            soup = BeautifulSoup(await response.text(), 'lxml')
            [img_urls.append(schema2 + a['href']) for a in soup.find_all('a')]


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            pbar = tqdm(total=2615, desc='Обработано изображений: ')
            main_soup = BeautifulSoup(await response.text(), 'lxml')
            urls = [schema + a['href'] for a in main_soup.find_all('a')]

            urls_tasks = []
            for link in urls:
                task = asyncio.create_task(get_links(session, link))
                urls_tasks.append(task)
            await asyncio.gather(*urls_tasks)

            download_tasks = []
            for link in img_urls:
                task = asyncio.create_task(find_images(session, link, pbar))
                download_tasks.append(task)
            await asyncio.gather(*download_tasks)


url = 'https://parsinger.ru/asyncio/aiofile/3/index.html'
schema = 'https://parsinger.ru/asyncio/aiofile/3/'
schema2 = 'https://parsinger.ru/asyncio/aiofile/3/depth2/'
img_urls = []
all_image_links = set()

start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

print(
    f'Cохранено изображений {len(os.listdir("images/"))} за {round(time.perf_counter() - start, 3)} сек')
print(get_folder_size('D:/Python/Parsing/images'))
