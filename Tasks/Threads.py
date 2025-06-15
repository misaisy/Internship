import concurrent.futures
import os
import glob


def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            word_count = len(text.split())
            print(f"{os.path.basename(file_path)}: {word_count} words\n")
            return word_count
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0


def main():
    folder = "text_files"
    file_pattern = os.path.join(folder, "*.txt")
    files = glob.glob(file_pattern)

    if not files:
        print("No files found!")
        return

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(count_words, files)

if __name__ == "__main__":
    main()