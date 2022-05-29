"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randrange as rnd

with open('numbers_2.txt', 'w', encoding='utf-8') as numbers:
    print(*[rnd(100) for _ in range(57)], file=numbers)

with open('numbers_2.txt', 'r', encoding='utf-8') as file_input:
    numbers = file_input.read().split()
    print(sum([int(i) for i in numbers]))
