"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать публичные методы получения полного имени
сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).
П.С. попытайтесь добиться вывода информации о сотруднике также через перегрузку
str. str(self) - вызывается функциями str, print и format.
Возвращает строковое представление объекта.
"""


class TypeStr:

    def __set__(self, instance, value):
        if type(value) == int:
            raise ValueError("Введите строковое значение")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    surname = TypeStr()
    name = TypeStr()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Employee: {self.surname} {self.name}')

    def get_total_income(self):
        print(f'Total income: {sum(self._income.values())}')

    def __str__(self):
        return f'Employee: {self.surname} {self.name}, ' \
               f'{self.position}, income: {sum(self._income.values())}'


emp_1 = Position('Natalia', 'Shneider', 'engineer', 25000, 1000)
emp_1.get_full_name()
emp_1.get_total_income()
print(emp_1.position)
print(emp_1)

emp_1.surname = 236548
emp_1.get_full_name()
