# Task 4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте
# в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False


    def go(self):
        print('Car going')


    def stop(self):
        print('Car stop')


    def turn(self,direction):
        print('Car direction to %s ' % direction)

    def show_speed(self):
        print(f'Current speed {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f' speed > 60')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f' speed > 40')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        #super().__init__()
        self.is_police = True

police = PoliceCar(180,"blue","Lada")
print(police.is_police)

t_car =  TownCar(80,"gren",'mazda')
print(t_car.show_speed())

