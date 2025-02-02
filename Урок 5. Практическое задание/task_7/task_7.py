"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
 содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
 средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import csv
import json

with open('firms.txt', 'r', encoding='utf-8') as file_input:
    obj = csv.DictReader(file_input, delimiter=' ', fieldnames='firm form revenue exps'.split())
    firm_dict = {}
    sum_profit = 0
    n = 0
    for i in obj:
        profits = int(i['revenue']) - int(i['exps'])
        firm_dict[i['firm']] = profits
        if profits > 0:
            sum_profit += profits
            n += 1
    average_profit = sum_profit / n
    result = [firm_dict, {'average_profit': average_profit}]
    with open('firms_output.json', 'w', encoding='utf-8') as file_output:
        json.dump(result, file_output, indent=4)
