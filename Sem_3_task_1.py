"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
# Мой навороченый вариант, try-exept добавила чисто попробовать на практике
from timeit import timeit
month = (input("Введите номер календарного месяца: "))
seasons_dict = {'зима': ['12', '1', '2'], 'весна': ['3', '4', '5'],
                'лето': ['6', '7', '8'],
                'осень': ['9', '10', '11']}
seasons_list = list(zip(seasons_dict.keys(), seasons_dict.values()))
try:
    if int(month) <= 12 and int(month) >= 1:
        for key in seasons_dict.keys():
            if month in seasons_dict.get(key):
                print(f'Словарь: время года - {key}')
        for key, value in seasons_list:
            if month in value:
                print(f'Список: время года - {key}')
    else:
        print("Введеное число не соотвествует месяцу")
except ValueError:
    print('Это не число, повторите ввод')

# после семинара

month = int(input("Введите номер календарного месяца: "))
seasons_dict = {12:'зима',1:'зима',2:'зима', 3:'весна', 4:'весна',
                5:'весна', 6: 'лето',7: 'лето', 8: 'лето', 9:'осень',
                10:'осень',11:'осень'}
print(f'Словарь:время года - {seasons_dict.get(month)}')
seasons_list = list(seasons_dict.values())
print(f'Список:время года - {seasons_list[month-1]}')

print(timeit("""month = int(input("Введите номер календарного месяца: "))
seasons_dict = {12:'зима',1:'зима',2:'зима', 3:'весна', 4:'весна',
                5:'весна', 6: 'лето',7: 'лето', 8: 'лето', 9:'осень',
                10:'осень',11:'осень'}
print(f'Словарь:время года - {seasons_dict.get(month)}')
seasons_list = list(seasons_dict.values())
print(f'Список:время года - {seasons_list[month-1]}')
""",number = 10))