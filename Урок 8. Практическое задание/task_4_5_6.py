"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
import datetime
import datetime


class Equipment():
    eq_dict = {}  # Снаряжение на балансе или в использовании
    eq_now = {}  # Снаряжение на данный момент на складе
    eq_list = []  # Список снаряжения полный
    dig_list = {'weight', 'year'}
    user = None
    ex_dict = {'owner': 'Club', 'weight': 0, 'year': datetime.datetime.now().year}  # Общие атрибуты

    def __init__(self, **kwargs):
        self.ex_dict.update(Equipment.ex_dict)
        for i in self.ex_dict:
            if i in kwargs:
                try:
                    self.ex_dict[i] = self.valid(kwargs[i], i)
                except Exception as ex:
                    print(ex)
        key = str(type(self)).split('.')[1][:-2]
        self.eq_dict[key] = self.eq_dict.setdefault(key, 0) + 1
        self.eq_now[key] = self.eq_now.setdefault(key, 0) + 1
        self.eq_list.append(self)

    def valid(self, value, key):
        if key in self.dig_list:
            return float(value)
        else:
            return value

    def set_dict(self):  # Установить все свойства снаряжения
        print(self.ex_dict)
        for i in self.ex_dict:
            if not self.ex_dict[i]:
                try:
                    self.ex_dict[i] = self.valid(input(f'Введите свойство {i}: '), i)
                    print(i, self.ex_dict[i])
                except Exception as ex:
                    print(ex)

    def move(self, user=None):  # Движение снаряжения. Предусмотрена выдача, возврат, передача.
        key = str(type(self)).split('.')[1][:-2]
        if not user:
            self.eq_now[key] += 1
        elif not self.user:
            self.eq_now[key] -= 1
        self.user = user

    def __str__(self):
        return str(self.ex_dict)


class Rope(Equipment):
    def __init__(self, **kwargs):
        self.ex_dict = {'length': None, "diameter": None, 'color': None, "type": None}
        super().dig_list.update(['length', 'diameter'])
        super().__init__(**kwargs)

    @staticmethod
    def valid(value, key):
        if key == 'type':
            if value in ('статика, динамика'):
                return value
            else:
                raise ValueError('Типы веревок бывают статика или динамика')
        return Equipment.valid(Equipment, value, key)


class Stove(Equipment):
    def __init__(self, **kwargs):
        self.ex_dict = {'power': None, "type": None}
        super().dig_list.update('power')
        super().__init__(**kwargs)

    @staticmethod
    def valid(value, key):
        if key == 'type':
            if value in ('резьбовая', 'цанговая'):
                return value
            else:
                raise ValueError('Типы горелок бывают резьбовая или цанговая')
        return Equipment.valid(Equipment, value, key)


class Tent(Equipment):
    def __init__(self, **kwargs):
        self.ex_dict = {'man': None, "frame_material": None, 'color': None, "frame_diameter": None}
        super().dig_list.update('frame_diameter')
        super().__init__(**kwargs)

    @staticmethod
    def valid(value, key):
        if key == 'frame_material':
            if value in ('алюминий', 'титан', 'стекловолокно', 'углеволокно'):
                return value
            else:
                raise ValueError('Такой тип каркаса не поддерживается клубом')
        elif key == 'man':
            return int(value)
        else:
            return Equipment.valid(Equipment, value, key)


# Часть первая. Заполняем склад.
input('На склад поступает три веревки длиной по 50 м, разных диаметров')
ropes = [Rope(length=50, diameter=12 - i) for i in range(3)]
input('На склад поступает три палатки')
tents = [Tent(weight=4.5, man=4, color='orange') for i in range(3)]
input('Для второй палатки установим детальные характеристики')
tents[1].set_dict()
input('На склад поступило пять горелок (мечта!)')
stoves = [Stove(weight=0.1, type="какая-то") for i in range(5)]

input('Проверяем характеристики объектов')
print(ropes[1], ropes[2], tents[0], tents[1], stoves[0], sep='\n')

# Часть вторая. Движение объектов
input('Проверяем, что есть на балансе и что есть на складе')
print("Hа балансе", Equipment.eq_dict)
print("На складе", Equipment.eq_now)

input('Передаем две палатки и горелку Рите')
tents[0].move('Рита')
tents[1].move('Рита')
stoves[0].move('Рита')

input('Проверяем, что есть на складе и на балансе. Баланс не изменился')
print("Hа балансе", Equipment.eq_dict)
print("На складе", Equipment.eq_now)

input('Рита вернула одну палатку на склад, а вторую отдала  Гале. Проверяем:')
tents[0].move()
tents[1].move('Галя')
print("На складе", Equipment.eq_now)
print("Вторая палатка у", tents[1].user)

"""
На этом кончилось 15 число и я кончила развлекаться.
На самом деле, можно допилить эту программу до ума и пользы;
Но для этого надо сделать ей нормальный интерфейс (и это я знаю как),
и нормальный способ хранения данных.
И это я пока не понимаю, как разумно сделать с классами. Если бы данные были
словарями, списками, множествами - можно загнать в файл/файлы через pickle или json,
а классы - нет. Так что я пока допиливать другие виды снаряжения не буду.
"""
