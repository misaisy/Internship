"""
Модуль для асинхронной загрузки веб-страниц.

Содержит функции:
- download_url: асинхронная загрузка одного URL
- main: основная функция для управления процессом загрузки
"""

import asyncio
import time

import aiohttp


async def download_url(session, url):
    """Асинхронная загрузка одного URL.

    :param session: HTTP-сессия
    :param url: url для запросов
    :return: текст ответа
    """
    async with session.get(url) as response:
        content = await response.text()
        # print("Установлено {}, размер: {} байт".format(url, len(content)))
        return content


async def main():
    """Управление процессом загрузки."""
    urls = ["https://google.com"] * 10
    start_time = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        tasks = [download_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    total_time = end_time - start_time
    print("Итоговое время: {:2f} секунд".format(total_time))

asyncio.run(main())
