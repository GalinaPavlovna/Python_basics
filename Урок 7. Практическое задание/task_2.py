"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""
from abc import ABC, abstractmethod


class Things(ABC):
    dict = {}

    @abstractmethod
    def get_consumptions(self):
        pass

    @abstractmethod
    def total_consumption(self):
        pass


class Clothes(Things):
    @staticmethod
    def con_suit(v):
        return v / 6.5 + 0.5

    @staticmethod
    def con_coat(h):
        return 2 * h + 0.3

    _dict = {"suit": con_suit, "coat": con_coat}

    def __init__(self, *args):
        self.things = []
        self.total = 0
        for i in range(0, len(args), 2):
            self.things.append((args[i], args[i + 1]))

    def consumption(self, thing, a):
        return self._dict[thing](a)

    def get_consumptions(self):
        for i in self.things:
            print(f'Расход ткани на {i[0]} - {self.consumption(i[0], i[1]):.2f}')

    @property
    def total_consumption(self):
        for i in self.things:
            self.total += self.consumption(i[0], i[1])
        return self.total


k1 = Clothes('suit', 1.6, 'coat', 2, 'coat', 3)
k1.get_consumptions()
print()
print(f"Общий расход ткани - {k1.total_consumption:.2f}")
