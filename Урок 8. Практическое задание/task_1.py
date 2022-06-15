"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data():
    day, month, year = None, None, None

    def __init__(self, string):
        Data.day_month_year = string
        try:
            self.valid_data(Data.day_month_year)
            self.analis_data()
        except ValueError as ex:
            print(ex)

    @staticmethod
    def valid_data(d):
        delimiter = d[-5]
        dict_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        day, month, year = [int(i) for i in d.split(delimiter)]
        if not month in dict_month:
            raise ValueError("Месяцев в году 12!")
        if not 0 < day <= dict_month[month]:
            raise ValueError("В месяце нет столько дней!")
        return True

    @classmethod
    def analis_data(cls):
        delimiter = cls.day_month_year[-5]
        cls.day, cls.month, cls.year = [int(i) for i in cls.day_month_year.split(delimiter)]


Data(input('Введите дату: '))
print(f"Месяц - {Data.month}, год - {Data.year}, дата - {Data.day}")
print(Data.valid_data('12/12/2004'))
