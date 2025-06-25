import time
import requests

URL = "https://google.com"

def url_requests(url, count, delay = 1):
    for i in range(count):
        response = requests.get(url)
        print("Запрос", i+1, "Статус ответа: ", response.status_code)
        time.sleep(delay)

start_time = time.perf_counter()
url_requests(URL, 10)
end_time = time.perf_counter() - start_time

print("Время выполнения:", end_time)