'''
Задача 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

'''


def calculation(n, res_num=0):
    if n == 0:
        return res_num
    res_num = res_num * 10 + n % 10
    n //= 10
    return calculation(n, res_num)


num = int(input('Введите число: '))
print(f'реверс числа {num} - {calculation(num)}')
