"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def delu(a, b):
    try:
        print(f'Результат  деления {int(a) / int(b):.2}')
    except ZeroDivisionError:
        print('На ноль делить не получается!')
    except ValueError:
        print('Кажется, вы ввели не число: это я делить не умею!')
    except Exception as e:
        print('Что-то пошло не так - ', e)


first = input('Введите первое число: ')
second = input('Введите второе число: ')
delu(first, second)
