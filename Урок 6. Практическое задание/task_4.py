"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
from random import randrange as rnd


class Car:
    colors = "Синий Желтый Красный Белый Бирюзовый Черный В_крапинку В_цветочек".split()

    def __init__(self, name):
        self.name = name
        self.speed = rnd(20, 100)
        self.color = self.colors[rnd(8)]
        self.is_police = False

    def run(self):
        print(f'Машина {self.name} {self.color} поехала')

    def stop(self):
        print(f"Машина{self.name} {self.color} остановилась")

    def turn(self, direction):
        if direction in 'налево направо нафиг'.split():
            print(f"Машина {self.name} {self.color} повернула {direction}")
        else:
            print(f'Машина {self.name} {self.color} повернуть {direction} не может')

    def show_speed(self):
        print(f'Машина {self.name} {self.color} движется со скоростью {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Машина {self.name} {self.color} превысила скорость!!!')
        else:
            super().show_speed()


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Машина {self.name} {self.color} превысила скорость!!!')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, name):
        super().__init__(name)
        self.is_police = True


class SportCar(Car):
    pass


k1 = SportCar('Vassa')
k1.turn('нафиг')
print(k1.__dict__)
k1.show_speed()
k2 = WorkCar('Fedor')
print(k2.__dict__)
k2.run()
k2.turn('вверх')
k2.show_speed()
k3 = PoliceCar('Nikola')
print(k3.__dict__)
k3.show_speed()
