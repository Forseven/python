# Task 2
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения
# данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса масфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода. Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.depth = 5
        self.weight_m = 25

    def weight(self):
        print((self._width * self._length * self.depth * self.weight_m) / 1000, 'т.')


my_road = Road(5000, 20)
my_road.weight()
