"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    surface_ro = 25
    thickness = 0.05

    def __init__(self, w, l):
        self._length = l
        self._width = w

    def asf_mass(self):
        return self._width * self._length * self.surface_ro * self.thickness / 10


r1 = Road(20, 5000)
r2 = Road(15, 1000)

print(f'Масса асфальта дороги 1 равна {r1.asf_mass()} тонн')
print(f'Масса асфальта дороги 2 равна {r2.asf_mass()} тонн')

"""
Только формула у вас неверная. Вы берете 25 кг/кв.м при толщине в 1 см. 
Значит, толщина должна измеряться в см. А вы ее в метрах подставляете.
К вашему примеру:
Площадь дороги - 100 000 кв.м.
Масса одного кв.м - 25*5=125 кг
Итоговая масса - 125*100 000= 12 500 000 кг = 12 500 т
"""
