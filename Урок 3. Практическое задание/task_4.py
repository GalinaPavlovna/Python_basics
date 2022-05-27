"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result*=x
    return 1 / result


try:
    osn = float(input('Введите действительное положительное число х: '))
    if osn<0:
        raise ValueError('Основание должно быть положительным')
    step = int(input('Введите целое отрицательное число у: '))
    if step > 0:
        raise ValueError('Степень должна быть отрицательной')
    print(f'x в степени y равен {my_func(osn, step):.6}')
except Exception as e:
    print('Что-то пошло не так -', e)
