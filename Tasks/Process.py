"""
Модуль вычисляющий числа Фибоначчи распределив вычисления между несколькими процессами.

Содержит функции:
- count_words: обработка файла
- main: основная функция для управления процессом обработки
"""
import concurrent.futures


def fib(n):
    """Вычисление чисел Фибоначчи.

    :param n: кол-во итераций
    :return: итоговое число
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    """Управление процессом вычисления."""
    numbers = [10000, 12000, 15000, 17000, 20000] * 4

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(fib, numbers))

    for i, res in enumerate(results):
        print("Результат {}: {}...".format(i + 1, str(res)[:50]))


if __name__ == "__main__":
    main()
