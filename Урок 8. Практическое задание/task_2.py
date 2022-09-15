"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivZeroMy(ValueError):
    def __init__(self, string=''):
        self.message = string

    def __str__(self):
        return f'Я тоже не люблю делить на ноль! {self.message}'


try:
    a = int(input("Делимое: "))
    b = int(input("Делитель: "))
    if b == 0:
        raise DivZeroMy()
    else:
        print(f'Частное - {a / b:.2f}')
except Exception as ex:
    print(ex)
