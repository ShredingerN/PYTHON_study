'''
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
'''


def count_numb(num, even=0, odd=0):
    if num == 0:
        print(f"Кол-во четных цифр - {even}, нечетных  - {odd}")
    else:
        cur_num = num % 10
        num = num // 10
        if cur_num % 2 == 0:
            even += 1
        else:
            odd += 1
        return count_numb(num, even, odd)


number = int(input("Введите число: "))
count_numb(number)
