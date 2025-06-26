import requests
import numpy as np

response = requests.get('https://api.github.com')
print(f"Статус-код: {response.status_code}")

array = np.arange(5)
print(f"Массив: {array}")