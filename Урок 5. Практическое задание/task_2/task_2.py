"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("poem.txt", 'r', encoding='utf-8') as poem:
    poem_list = poem.readlines()
    print(f'Всего строк в файле - {len(poem_list)}')
    [print(f'В строке {i + 1} {len(poem_list[i].split())} слов') for i in range(len(poem_list))]
