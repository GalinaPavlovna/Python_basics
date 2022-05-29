"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
from random import randrange as rnd
my_list = [rnd(135) for _ in range(13)]
print('Исходный список - ', *my_list)
print('Список через list comprehension', *[my_list[i] for i in range(1, 13) if my_list[i]>my_list[i-1]])
result_list=[]
for i in range(1, 13):
    if my_list[i]>my_list[i-1]:
        result_list.append(my_list[i])
print('Список стандартным способом: ', *result_list)
