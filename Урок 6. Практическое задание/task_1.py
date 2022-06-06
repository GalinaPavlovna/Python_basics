"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep
from itertools import cycle


class TrafficLight:
    color = 'Красный'

    def running(self, n):
        colors = 'Красный Желтый Зеленый'.split()
        times = (7, 2, 5)
        dict_1 = dict(zip(colors, times))
        conditions = cycle(colors)
        for i in range(n * 3):
            self.color = next(conditions)
            print("Переключение светофора - теперь", self.color)
            sleep(dict_1[self.color])


light = TrafficLight()
print(light.color)
light.running(2)
