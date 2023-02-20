# Задача 2: Найдите сумму цифр трехзначного числа.

print("Введите трехзначное положительное число: ")
number = int(input())
if 100 <= number <= 999:
    fig_1 = number % 10
    fig_2 = (number // 10) % 10
    fig_3 = number // 100
    sum_fig = fig_1 + fig_2 + fig_3
    print(f"Сумма цифр введенного числа равна : {sum_fig}")
else:
    print("Вы ввели не трехзначное число!")