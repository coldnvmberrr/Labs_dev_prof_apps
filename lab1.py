"""
Лабораторная работа №1
Михайлова Александра гр. ВТАСбзу-21
Вариант 6

Из списка A удалить те цепочки четных элементов, в которых есть хотя бы один элемент из списка B.
Пример: список A[9]: 3 2 4 5 2 3 2 6 5
список B[6]: 1 3 4 7 8 9
список A после удаления примет вид:
A[7]: 3 5 2 3 2 6 5.
"""
from random import randint


def check_chain_in_list_b(chain, list_b):
    """ Проверка цепочки четных элементов есть ли хотя бы один элемент из списка B """
    for item in chain:
        if item in list_b:
            return True
    return False


def sort(list_a, list_b):
    """ Сортировка списка A по требованиям задания"""
    result = []
    chain_of_even_elements = []  # цепочка четных элементов
    for number in list_a:  # проходимся по массиву
        if number % 2 == 0:
            chain_of_even_elements.append(number)
        else:
            if not check_chain_in_list_b(chain_of_even_elements, list_b):
                result += chain_of_even_elements
            chain_of_even_elements = []
            result.append(number)
    if len(chain_of_even_elements) != 0 and not check_chain_in_list_b(chain_of_even_elements, list_b):
        result += chain_of_even_elements
    return result


def input_list(n):
    """ Ввод элементов списка c клавиатуры"""
    try:
        new_list = []
        for _ in range(n):
            new_list.append(int(input("Введите элемент списка: ")))
        return new_list
    except ValueError as e:
        print("Ошибка. Введите целое число.")
        exit()


def random_list(n):
    """Генерация элементов списка"""
    new_list = []
    for _ in range(n):
        new_list.append(randint(1, 10))
    return new_list


def input_data():
    """Ввод списка"""
    try:
        n = int(input("Введите количество элементов в списке: "))
        print("Выберите режим ввода \n1 - ввод с клавиатуры \n2 - автоматическая генерация")
        mode = int(input())

    except ValueError:
        print("Ошибка. Введите целое число.")
        exit()

    if not mode == 1 and not mode == 2:
        print("Ошибка. Введите корректное значение")
        exit()

    if mode == 1:
        return input_list(n)
    else:
        return random_list(n)


def main():
    print("Ввод списка А")
    list_a = input_data()

    print("Ввод списка B")
    list_b = input_data()

    result = sort(list_a, list_b)
    print(f'Список A[{len(list_a)}]: {list_a}')
    print(f'Список B[{len(list_b)}]: {list_b}')
    print(f'Результат A[{len(result)}]: {result}')


if __name__ == "__main__":
    main()
