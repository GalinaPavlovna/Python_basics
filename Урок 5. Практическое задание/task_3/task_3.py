"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

with open('numbers_eng.txt', 'r', encoding='utf-8') as file_input:
    with open('numbers_rus.txt', 'w', encoding='utf-8') as file_output:
        russian = "ноль один два три четыре пять шесть семь восемь девять".split()
        for s in file_input:
            string_list = s.split()
            string_list.pop(0)
            string_list.insert(0, russian[int(string_list[1])])
            print(' '.join(string_list), file=file_output)
