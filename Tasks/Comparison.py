"""
Модуль собирающий данные с 50-URL адресов тремя способами и сравнивающий их.

Содержит функции:
- download_one: загрузка одного URL
- async_download: асинхронный сбор
- thread_download: многопоточный сбор
- process_download: многопроцессорный сбор
- compare: сравнение способов сбора данных
"""
import asyncio
import concurrent.futures
import time

import aiohttp

import requests


async def download_one(session, url):
    """Загрузка одного URL.

    :param session: HTTP-сессия aiohttp
    :param url: URL-адрес
    :return: статус или ошибка
    """
    try:
        async with session.get(url) as response:
            await response.read()
            return response.status
    except Exception as e:
        return str(e)


async def async_download(urls):
    """Асинхронный сбор.

    :param urls: массив URL-адресов
    :return: время выполнения
    """
    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        tasks = [download_one(session, url) for url in urls]
        await asyncio.gather(*tasks)

    async_time = time.perf_counter() - start
    return async_time


def thread_download(urls):
    """Многопоточный сбор.

    :param urls: массив URL-адресов
    :return: время выполнения
    """
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(requests.get, urls)

    thread_time = time.perf_counter() - start

    return thread_time


def process_download(urls):
    """Многопроцессорный сбор.

    :param urls: массив URL-адресов
    :return: время выполнения
    """
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(requests.get, urls)

    process_time = time.perf_counter() - start
    return process_time


def compare():
    """Сравнение способов сбора данных."""
    urls = ["https://google.com"] * 50

    async_time = asyncio.run(async_download(urls))
    print(f"Асинхронный: {async_time:.2f} sec")

    print(f"Многопоточный: {thread_download(urls):.2f} sec")

    print(f"Многопроцессорный: {process_download(urls):.2f} sec")


if __name__ == "__main__":
    compare()
