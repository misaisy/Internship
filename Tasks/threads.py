"""
Модуль, обрабатывающий папку с текстовыми файлами в несколько потоков.

Содержит функции:
- count_words: обработка файла
- main: основная функция для управления процессом обработки
"""

import concurrent.futures
import glob
import os
import logging.config

# logging.basicConfig(
#     level=logging.INFO,
#     filename="tg_log.log",
#     filemode="a",
#     encoding="utf-8",
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )

logging.config.dictConfig(
    {
        "version": 1,
        "formatters": {
            "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"}
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
                "level": "INFO",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "file_processing.log",
                "formatter": "standard",
                "level": "DEBUG",
                "encoding": "utf-8",
            },
        },
        "loggers": {
            "": {"handlers": ["console", "file"], "level": "DEBUG", "propagate": True}
        },
    }
)

logger = logging.getLogger(__name__)


def count_words(file_path):
    """Обработка файла.

    :param file_path: путь к файлу
    :return: кол-во слов в файле или текст ошибки
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            word_count = len(text.split())
            print("{}: {} words".format(os.path.basename(file_path), word_count))
            logger.info(
                "Обработан файл %s: %d слов", os.path.basename(file_path), word_count
            )
            return word_count
    except Exception as e:
        error_msg = f"Ошибка при обработке {os.path.basename(file_path)}: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return error_msg


def main():
    """Управление процессом обработки."""
    logger.info("Запуск обработки файлов")
    folder = "text_files"
    file_pattern = os.path.join(folder, "*.txt")
    files = glob.glob(file_pattern)

    if not files:
        logger.warning("Файлы не найдены в папке %s", folder)
        print("Файлы не найдены")
        return

    logger.debug("Найдено файлов для обработки: %d", len(files))
    logger.debug("Список файлов: %s", files)

    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(count_words, files)
    except Exception as e:
        logger.critical(
            "Критическая ошибка в основном потоке: %s", str(e), exc_info=True
        )
    finally:
        logger.info("Обработка файлов завершена")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception("Непредвиденная ошибка в точке входа")
