import concurrent.futures
import os
import glob


def count_words(file_path):
    """
        Обработка файла

        :param file_path: путь к файлу
        :return: кол-во слов в файле или текст ошибки
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            word_count = len(text.split())
            print(f"{os.path.basename(file_path)}: {word_count} words\n")
            return word_count
    except Exception as e:
        return str(e)


def main():
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