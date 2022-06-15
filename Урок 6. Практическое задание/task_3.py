"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
from random import randrange as rnd


class Worker():
    name = None
    surname = None
    position = None
    _income = {'wage': None, "bonus": None}
    positions = "царь царевич король королевич сапожник портной".split()
    wages = dict(zip(positions, (100000, 90000, 50000, 45000, 500, 400)))


class Position(Worker):

    def __init__(self):
        self.name = input("Введите имя пользователя: ")
        self.surname = input("Введите фамилию пользователя: ")
        self.position = input("Введите должность: ")
        while self.position not in self.positions:
            self.position = input("такой должности нет! Введите должность: ")
        self._income['wage'] = self.wages[self.position]
        self._income['bonus'] = rnd(10) * self._income['wage'] / 10

    def __str__(self):
        return f'{self.surname} {self.name}, должность {self.position}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


m1 = Position()
print(m1)
print(m1.get_total_income())
