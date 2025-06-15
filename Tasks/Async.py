import asyncio
import aiohttp
import time


async def download_url(session, url):
    async with session.get(url) as response:
        content = await response.text()
        print(f"Установлено {url}, размер: {len(content)} байт")
        return content


async def main():
    urls = ["https://google.com"] * 10

    start_time = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        tasks = [download_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Итоговое время: {total_time:2f} секунд")

asyncio.run(main())