"""
Пусть дана некоторая директория (папка).
Посчитайте количество файлов в данной директории (папке) и выведите на экран.
"""

import os

DIRECTORY = '../test_directory'


def main():
    try:
        files = [file for file in os.listdir(DIRECTORY) if os.path.isfile(f'{DIRECTORY}/{file}')]
        print(len(files))
    except FileNotFoundError:
        print('Некорректный путь директории')


if __name__ == "__main__":
    main()
