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
import requests
from aiohttp_retry import RetryClient, ExponentialRetry
from bs4 import BeautifulSoup
from tqdm import tqdm
import os


def get_links(url):
    schema = 'https://parsinger.ru/asyncio/aiofile/2/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    [links.append(schema + a['href']) for a in soup.find_all('a')]


def get_folder_size(filepath, size=0):
    for root, _, files in os.walk(filepath):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size


async def download_image(session, url, img_name):
    async with aiofiles.open(f'images/{img_name}', mode='wb') as file:
        async with session.get(url) as response:
            async for chunck in response.content.iter_chunked(2048):
                await file.write(chunck)


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


async def main():
    async with aiohttp.ClientSession() as session:
        pbar = tqdm(total=449, desc='Обработано изображений: ')
        tasks = []
        for link in links:
            task = asyncio.create_task(find_images(session, link, pbar))
            tasks.append(task)
        await asyncio.gather(*tasks)
        pbar.close()


url = 'https://parsinger.ru/asyncio/aiofile/2/index.html'
links = []
all_image_links = set()
get_links(url)

start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

print(
    f'Cохранено изображений {len(os.listdir("images/"))} за {round(time.perf_counter() - start, 3)} сек')
print(get_folder_size('D:/Python/Parsing/images'))
