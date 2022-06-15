"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class ListDigitError(ValueError):
    def __init__(self, string=''):
        self.message = string

    def __str__(self):
        return f'В списке должны быть только числа! Вы ввели {self.message}'


def valid(i):
    try:
        return float(i)
    except Exception:
        raise ListDigitError(i)


my_list = []
print('Заполните список числами.  & - признак конца ввода.')
n = input('Введите число: ')
while n != '&':
    try:
        my_list.append(valid(n))
    except Exception as ex:
        print(ex)
    finally:
        n = input("Следующее число: ")
print(*my_list)
