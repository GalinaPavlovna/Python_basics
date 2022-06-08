"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:

    def __init__(self, l):
        self.wigth = len(l)
        self.high = len(l[0])
        for i in l:
            if len(i) != self.high:
                raise ValueError('Это не матрица!')
            for j in i:
                if type(j) not in (int, float):
                    raise ValueError('Элементы матрицы должны быть числами!')
        self.matr = l


    def __str__(self):
        s = '\n'.join([''.join([str(j).ljust(4, ' ') for j in i]) for i in self.matr])
        return s

    def __add__(self, other):
        try:
            if type(other) != Matrix:
                raise ValueError("Матрицы складываются только с матрицами!")
            if self.wigth != other.wigth or self.high != other.high:
                raise ValueError('Нельзя сложить матрицы разного размера!')
            sum_matr = [[self.matr[i][j] + other.matr[i][j] for j in range(self.high)] for i in range(self.wigth)]
            return Matrix(sum_matr)
        except Exception as ex:
            return f'Сложению не подлежит - {ex}'


m1 = Matrix([[1, 5, 3], [4, 5, 27]])
m2 = Matrix([[10, 20, 30], [40, 50, 60]])
print (m1)
print()
print(m1 + m2)
