"""
Модуль выполнения 10 HTTP-запросов разными способами и сверка времени выполнения.

Содержит функции:
- sync_request: синхронный запрос
- async_request: асинхронный запрос
- run_sync: синхронный подход
- run_async: асинхронный подход
- run_threaded: многопоточный подход
- run_process: многопроцессорный подход
"""

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import aiohttp

import requests

URL = "http://www.skuad-dev.nots-fns.ru/docs#/"
REQUESTS = 100


def sync_request(url):
    """Синхронный запрос.

    :param url: url для запросов
    :return: код ответа или ошибка
    """
    try:
        response = requests.get(url)
        return response.status_code
    except Exception as e:
        return str(e)


async def async_request(session, url):
    """Асинхронный запрос.

    :param session: экземпляр aiohttp.ClientSession для выполнения запросов
    :param url: url для запросов
    :return: код ответа или ошибка
    """
    try:
        async with session.get(url) as response:
            return response.status_code
    except Exception as e:
        return str(e)


def run_sync():
    """Синхронный подход.

    :return: время выполнения
    """
    start = time.time()
    for _ in range(REQUESTS):
        sync_request(URL)
    return time.time() - start


async def run_async():
    """Асинхронный подход.

    :return: время выполнения
    """
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [async_request(session, URL) for _ in range(REQUESTS)]
        await asyncio.gather(*tasks)
    return time.time() - start


def run_threaded():
    """Многопоточный подход.

    :return: время выполнения
    """
    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        list(executor.map(sync_request, [URL] * REQUESTS))
    return time.time() - start


def run_process():
    """Многопроцессорный подход.

    :return: время выполнения
    """
    start = time.time()
    with ProcessPoolExecutor(max_workers=10) as executor:
        list(executor.map(sync_request, [URL] * REQUESTS))
    return time.time() - start


if __name__ == "__main__":
    sync_time = run_sync()
    print(f"Синхронное выполнение: {sync_time:.2f} сек")

    async_time = asyncio.run(run_async())
    print(f"Асинхронное выполнение: {async_time:.2f} сек")

    thread_time = run_threaded()
    print(f"Многопоточное выполнение: {thread_time:.2f} сек")

    process_time = run_process()
    print(f"Многопроцессорное выполнение: {process_time:.2f} сек")
