"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = 'Unknown'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    title = 'pen'

    def draw(self):
        super().draw()
        print(f'Эта {self.title} рисует тоненько и затейливо')


class Pencil(Stationery):
    title = 'pencil'

    def draw(self):
        super().draw()
        print(f'Этот {self.title} рисует плавно и нежно')


class Handle(Stationery):
    title = 'handle'

    def draw(self):
        super().draw()
        print(f'Этот {self.title} рисует резко и ярко')


s1 = Stationery()
s1.draw()
s2 = Pen()
s2.draw()
s3 = Pencil()
s3.draw()
s4 = Handle()
s4.draw()
