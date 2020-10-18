# Task 5
# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.


class Stationery():
    def __init__(self,name):
        self.name = name

    def draw(self):
        print('Draw %s ' % self.name)


class Pen(Stationery):
    def draw(self):
        print('Draw pen %s ' % self.name)


class Pencil(Stationery):
    def draw(self):
        print('Draw pencil %s ' % self.name)


class Handle(Stationery):
    def draw(self):
        print('Draw handle %s ' % self.name)
handl = Handle("Blue_name")
handl.draw()

pen = Pen('Name_pen')
pen.draw()

pencil = Pencil("Eric")
pencil.draw()