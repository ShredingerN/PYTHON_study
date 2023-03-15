'''
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод
running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''

# попробовала с цветом текста поиграть
from time import sleep
from colorama import init, Fore

init()


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        print(Fore.RED + f'{self.color[0]}')
        sleep(7)
        print(Fore.YELLOW + f'{self.color[1]}')
        sleep(2)
        print(Fore.GREEN + f'{self.color[2]}')
        sleep(5)


lights = TrafficLight()
lights.running()

# этот код короче, без раскрашивания.

# class TrafficLight:
#     __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}
#
#     def running(self):
#         for key, value in self.__color.items():
#             print(key)
#             sleep(value)
#
#
# lights = TrafficLight()
# lights.running()
