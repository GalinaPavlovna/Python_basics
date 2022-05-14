"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_1(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    return my_list[2] + my_list[1]


def my_func_2(a, b, c):
    return a + b + c - min((a, b, c))


try:
    m, n, k = int(input('Введите три числа: ')), int(input()), int(input())
    print(f"Сумма двух самых больших {my_func_1(m, n, k)}")
    print(f"А может быть {my_func_2(m, n, k)}?")
except ValueError:
    print('Кажется, это не числа')
except Exception as e:
    print(f"Что-то пошло не так - {e}")
