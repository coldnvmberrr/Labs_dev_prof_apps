"""
Лабораторная работа №2
Михайлова Александра гр. ВТАСбзу-21
Вариант 6

Ввод элементов списка должен быть доступен путем автоматической генерации.
Необходимо использовать библиотеку numpy.
Результаты выполнения должны сохраняться в файл (исходные данные и результат обработки).
Исходный код должен быть откомментирован
Необходимо реализовать правильную декомпозицию программы на методы.

Выполнить обработку элементов прямоугольной матрицы A, имеющей N строк и M столбцов.
Найти сумму элементов всей матрицы.
Определить, какую долю в этой сумме составляет сумма элементов каждого столбца.
Результат оформить в виде матрицы из N + 1 строк и M столбцов.
"""
import numpy as np

FILE_PATH = "./lab2/logs.txt"


def calculation(matrix: np.ndarray, n: int, m: int):
    """Вычисление общей суммы и суммы по столбцам """
    sum = 0
    sum_by_columns = [0 for _ in range(m)]  #иницализация суммы колон
    for i in range(n):
        row = matrix[i]
        for j in range(m):
            sum += row[j]
            sum_by_columns[j] += row[j]
    return sum, sum_by_columns


def write_matrix(file, matrix, header):
    """Запись в файл"""
    file.writelines([header])
    for line in matrix:
        file.write('\n')
        np.savetxt(file, line, fmt='%.0f', newline=' ')
    file.write('\n \n')


def main():
    try:
        n = int(input("Введите кол-во строк: "))
        m = int(input("Введите кол-во столбцов: "))
    except ValueError:
        print("Ошибка. Введите целое число.")
        exit()
    file = open(FILE_PATH, "w", encoding="utf-8")
    a = np.random.randint(1, 30, size=(n, m))
    write_matrix(file, a, "Исходный список:")
    sum, sum_by_columns = calculation(a, n, m)
    result = [i * 100 // sum for i in sum_by_columns]
    a = np.vstack([a, result])
    write_matrix(file, a, "Результат:")
    file.close()


if __name__ == "__main__":
    main()
