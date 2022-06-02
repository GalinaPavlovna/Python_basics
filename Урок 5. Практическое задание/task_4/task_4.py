"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

"""

with open('people.txt', 'r', encoding='utf=8') as salary:
    salary_smoll = []
    average = 0
    n = 0
    for i in salary:
        men, sal = i.split()
        if float(sal) < 20000:
            salary_smoll.append(men)
        average += float(sal)
        n += 1
    print('Люди с небольшой зарплатой:', *salary_smoll, sep='\n')
    print(f"Средняя зарплата - {average / n :.2f}")
