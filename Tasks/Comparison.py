import asyncio
import aiohttp
import time
import concurrent.futures
import requests


async def async_download(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        await asyncio.gather(*tasks)


def thread_download(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(requests.get, urls)


def process_download(urls):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(requests.get, urls)


def compare():
    urls = ["https://google.com"] * 50

    start = time.perf_counter()
    asyncio.run(async_download(urls))
    async_time = time.perf_counter() - start

    start = time.perf_counter()
    thread_download(urls)
    thread_time = time.perf_counter() - start

    start = time.perf_counter()
    process_download(urls)
    process_time = time.perf_counter() - start

    print(f"Async: {async_time:.2f} sec")
    print(f"Threads: {thread_time:.2f} sec")
    print(f"Processes: {process_time:.2f} sec")


if __name__ == "__main__":
    compare()