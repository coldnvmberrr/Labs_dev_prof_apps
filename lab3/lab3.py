"""
Лабораторная работа №3
Михайлова Александра гр. ВТАСбзу-21
Вариант 6

Пусть дан файл data.csv, в котором содержится информация в соответствии с вариантом:
Считайте информацию из файла в соответствующую структуру (словарь):
2.1. Выведите информацию об объектах, отсортировав их по одному полю (строковому).
2.2. Выведите информацию об объектах, отсортировав их по одному полю (числовому).
2.3. Выведите информацию, соответствующую какому-либо критерию (например, для студентов - тех, у кого возраст больше какого-либо значения)

Добавьте к программе возможность сохранения новых данных обратно в файл.
История проездов автомобилей: №, дата и время, номерной знак, марка автомобиля

"""
import csv
from datetime import datetime

DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'


def sort(array, key, reverse=False):
    """Сортировка"""
    return sorted(array, key=lambda obj: obj[key], reverse=reverse)


def read_csv(file_path):
    """Чтение и получение информации с файла и сериализация в словарь"""
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        result = []
        for row in reader:
            if row[0] == 'id':
                continue
            result.append({
                'id': row[0],
                'datetime': datetime.strptime(row[1], DATETIME_FORMAT),
                'number': row[2],
                'model': row[3]
            })
        return result


def write_csv(file_path, objects):
    """Запись в файл"""
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'datetime', 'number', 'model'])
        for obj in objects:
            writer.writerow([obj['id'], obj['datetime'].strftime(DATETIME_FORMAT), obj['number'], obj['model']])


def print_history_drive_cars(array):
    """Вывод истории проездов автомобилей"""
    for item in array:
        print(
            f"№ {item['id']}, "
            f"Дата и время: {item['datetime'].strftime(DATETIME_FORMAT)}, "
            f"Номерной знак: {item['number']}, "
            f"Марка автомобиля: {item['model']}"
        )


def datetime_more_1_10_2022(obj):
    """Дата и время больше 1.10.2022"""
    return obj['datetime'] > datetime(2022, 10, 1)


def input_car(data):
    """Добавление новых данных в список объектов"""
    number = input("Введите номерной знак: ")
    model = input("Введите марку автомобили: ")
    new_object = {
        'id': len(data) + 1,
        'datetime': datetime.now(),
        'number': number,
        'model': model
    }
    data.append(new_object)
    return data


def main():
    data = read_csv('data.csv')

    print('Сортировка по модели')
    sorted_by_model = sort(data, key='model')
    print_history_drive_cars(sorted_by_model)

    print('Сортировка по id')
    sorted_by_id = sort(data, key='id')
    print_history_drive_cars(sorted_by_id)

    print('Фильтрация по дате и времени > 1.10.2022')
    filter_by_datetime = filter(datetime_more_1_10_2022, data)
    print_history_drive_cars(filter_by_datetime)

    print('Добавление новых данных в список объектов')
    data = input_car(data)
    print_history_drive_cars(data)
    write_csv('data.csv', data)


if __name__ == "__main__":
    main()
