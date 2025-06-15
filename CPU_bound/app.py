import os
import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

NUMBERS = list(range(1, 1001))


def calculate_factorial(n):
    """
        Вычисление факториала

        :param n: число для вычисления
        :return: результат вычисления
    """
    result = 1
    for _ in range(1000):
        result = math.factorial(n)
    return result


def run_sync():
    """
        Синхронный подход

        :return: время выполнения
    """
    start = time.time()
    for n in NUMBERS:
        calculate_factorial(n)
    return time.time() - start


def run_threaded():
    """
        Многопоточный подход

        :return: время выполнения
    """
    start = time.time()
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(calculate_factorial, NUMBERS)
    return time.time() - start


def run_process():
    """
        Многопроцессорный подход

        :return: время выполнения
    """
    start = time.time()
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(calculate_factorial, NUMBERS)
    return time.time() - start


if __name__ == "__main__":

    sync_time = run_sync()
    print(f"Синхронное выполнение: {sync_time:.4f} сек")

    thread_time = run_threaded()
    print(f"Многопоточное выполнение: {thread_time:.4f} сек")

    process_time = run_process()
    print(f"Многопроцессорное выполнение: {process_time:.4f} сек")