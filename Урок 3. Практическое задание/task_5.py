"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
f = 1
result = 0
while f:
    string = input('Введите строку чисел, разделенных пробелом. Если вы хотите закончить - нажмите @ вместо числа:\n')
    if '@' in string:
        f=0
        string = string.replace('@', '')
    string=string.split()
    result = sum([int(i) for i in string], result)
    print('На данный момент ваша сумма', result)
