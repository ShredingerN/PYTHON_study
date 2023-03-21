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


class PositiveNotZero:

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Значение должно быть положительным и не равно 0")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    density = 25
    thikness = 0.05
    width = PositiveNotZero()
    length = PositiveNotZero()

    def __init__(self, width, length):
        self._length = length
        self._width = width

    def mass_asf(self):
        mass = self._length * self._width * self.density * self.thikness / 1000
        print(f'Масса асфальта для дорожного полотна шириной {self._width} м, '
              f'длиной {self._length} м равна - {mass} тонн')


road = Road(20, 7000)
road.mass_asf()
road.width = 20
road.length = 0
road.mass_asf()
