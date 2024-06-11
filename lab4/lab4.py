import csv
from datetime import datetime

DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'


class PassagingCarInfo:
    """Информация о проезда автомобиля"""

    def __init__(self, id, datetime, number, model):
        setattr(self, '_id', id)
        setattr(self, '_datetime', datetime)
        setattr(self, '_number', number)
        setattr(self, '_model', model)

    def __repr__(self):
        return (
            f"№ {self._id}, "
            f"Дата и время: {self._datetime.strftime(DATETIME_FORMAT)}, "
            f"Номерной знак: {self._number}, "
            f"Марка автомобиля: {self._model}"
        )

    def __str__(self):
        return f'{self._id}, {self._datetime.strftime(DATETIME_FORMAT)}, {self._number}, {self._model}'

    def __getitem__(self, index):
        return getattr(self, index)

    @property
    def id(self):
        return self._id

    @property
    def number(self):
        return self._number

    @property
    def model(self):
        return self._model

    @property
    def datetime(self):
        return self._datetime

    @staticmethod
    def create(row):
        """Создание информации о проезде автомобиля"""
        return PassagingCarInfo(
            id=int(row[0]),
            datetime=datetime.strptime(row[1], DATETIME_FORMAT),
            number=row[2],
            model=row[3]
        )


class HistoryPassagingCars:
    """История проездов автомобилей"""

    def __init__(self, file_path):
        self.file_path = file_path
        self.cars = [PassagingCarInfo.create(row) for row in self.read_csv(file_path)[1:]]

    def __getitem__(self, index):
        return self.cars[index]

    def __iter__(self):
        for car in self.cars:
            yield car

    def sort(self, key, reverse=False):
        """Сортировка"""
        return sorted(self.cars, key=lambda obj: obj[key], reverse=reverse)

    @staticmethod
    def read_csv(file_path):
        """Чтение и получение информации с файла """
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            return [row for row in reader]

    def write_csv(self):
        """Запись истории в файл csv"""
        with open(self.file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'datetime', 'number', 'model'])
            for obj in iter(self):
                writer.writerow([obj.id, obj.datetime.strftime(DATETIME_FORMAT), obj.number, obj.model])

    @staticmethod
    def datetime_more_1_10_2022(obj):
        """Дата и время больше 1.10.2022"""
        return obj.datetime > datetime(2022, 10, 1)

    @staticmethod
    def print(cars):
        for car in cars:
            print(repr(car))

    def sorted_by_model(self):
        """Сортировка по модели"""
        self.print(self.sort(key='model'))

    def sorted_by_id(self):
        """Сортировка по id"""
        self.print(self.sort(key='id'))

    def filter_by_datetime(self):
        """Фильтрация по дате и времени"""
        self.print(filter(self.datetime_more_1_10_2022, self.cars))

    def input_car(self):
        """Добавление новых данных в список объектов"""
        number = input("Введите номерной знак: ")
        model = input("Введите марку автомобили: ")
        new_object = PassagingCarInfo(
            id=len(self.cars) + 1,
            datetime=datetime.now(),
            number=number,
            model=model
        )
        self.cars.append(new_object)


def main():
    history = HistoryPassagingCars(file_path='data.csv')

    print('Сортировка по модели')
    history.sorted_by_model()

    print('Сортировка по id')
    history.sorted_by_id()

    print('Фильтрация по дате и времени > 1.10.2022')
    history.filter_by_datetime()

    print('Добавление новых данных в список объектов')
    history.input_car()
    history.print(history.cars)
    history.write_csv()


if __name__ == "__main__":
    main()
