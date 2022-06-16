"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber():
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            s = args[0].split('+')
            self.re = float(s[0].strip())
            self.im = float(s[1].strip()[:-1])
        elif len(args) == 2 and isinstance(args[0], (float, int)) and isinstance(args[1], (float, int)):
            self.re = args[0]
            self.im = args[1]
        else:
            raise ValueError(f'Невозможно превратить в комплексное число {args} ')

    def __str__(self):
        return f'{self.re} + {self.im}i'

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re + other.re, self.im + other.im)
        elif isinstance(other, (float, int)):
            return ComplexNumber(self.re + other, self.im)
        else:
            raise ValueError('Комплексные числа можно складывать только с числами.')

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re * other.re - self.im * other.im,
                                  self.im * other.re + self.re * other.im)
        elif isinstance(other, (float, int)):
            return ComplexNumber(self.re * other, self.im * other)
        else:
            raise ValueError('Комплексные числа можно умножать только на числа.')

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            c = ComplexNumber(other.re, -1 * other.im)
            c1 = self * c
            c2 = other * c
            return ComplexNumber(c1.re / c2.re, c1.im / c2.re)
        elif isinstance(other, (float, int)):
            return ComplexNumber(self.re / other, self.im / other)
        else:
            raise ValueError('Комплексные числа можно делить только на числа.')

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re - other.re, self.im - other.im)
        elif isinstance(other, (float, int)):
            return ComplexNumber(self.re - other, self.im)
        else:
            raise ValueError('Комплексные числа можно вычитать только с числами.')


c1 = ComplexNumber('4+7.5i')
c2 = ComplexNumber(3, -2)
print(c1 + c2, c1 - c2, c1 * c2, c1 / c2, sep='\n')

# Особенно интересно это делать, зная, что в python есть встроенный тип комплексных чисел