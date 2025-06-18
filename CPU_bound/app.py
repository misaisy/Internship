"""
Модуль для вычисления факториала и замера времени выполнения.

Содержит функции:
- calculate_factorial: вычисление факториала
- run_sync: синхронный подход
- run_threaded: многопоточный подход
- run_process: многопроцессорный подход
"""

import math
import os
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

NUMBERS = list(range(1, 1001))


def calculate_factorial(n):
    """Вычисление факториала.

    :param n: число для вычисления
    :return: результат вычисления
    """
    result = 1
    for _ in range(1000):
        result = math.factorial(n)
    return result


def run_sync():
    """Синхронный подход.

    :return: время выполнения
    """
    start = time.time()
    for n in NUMBERS:
        calculate_factorial(n)
    return time.time() - start


def run_threaded():
    """Многопоточный подход.

    :return: время выполнения
    """
    start = time.time()
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(calculate_factorial, NUMBERS)
    return time.time() - start


def run_process():
    """Многопроцессорный подход.

    :return: время выполнения
    """
    start = time.time()
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(calculate_factorial, NUMBERS)
    return time.time() - start


if __name__ == "__main__":

    sync_time = run_sync()
    print("Синхронное выполнение: {:.4f} сек".format(sync_time))

    thread_time = run_threaded()
    print("Многопоточное выполнение: {:.4f} сек".format(thread_time))

    process_time = run_process()
    print("Многопроцессорное выполнение: {:.4f} сек".format(process_time))
