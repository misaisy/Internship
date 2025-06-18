"""
Модуль, обрабатывающий папку с текстовыми файлами в несколько потоков.

Содержит функции:
- count_words: обработка файла
- main: основная функция для управления процессом обработки
"""
import concurrent.futures
import glob
import os


def count_words(file_path):
    """Обработка файла.

    :param file_path: путь к файлу
    :return: кол-во слов в файле или текст ошибки
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            word_count = len(text.split())
            print("{}: {} words".format(os.path.basename(file_path), word_count))
            return word_count
    except Exception as e:
        return str(e)


def main():
    """Управление процессом обработки."""
    folder = "text_files"
    file_pattern = os.path.join(folder, "*.txt")
    # Можно использовать pathlib (Path)
    files = glob.glob(file_pattern)

    if not files:
        print("Файлы не найдены")
        return

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(count_words, files)


if __name__ == "__main__":
    main()
