"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

"""

list_words = ['attribute', 'класс', 'функция', 'type']

try:
    for el in list_words:
        f = bytes(el, 'ascii')
        print(
            f'тип переменной: {type(f)}, содержание:  {f}')
except UnicodeEncodeError:
    print('!!!Не возможно обработать кириллицу, задайте слова на латинице')
