# Задание 3.
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.

print("Введите целое положительное число: ")
n = int(input())
sum_string = str(n) + str(n * n) + str(n * n * n)
print(f"Сумма n+nn+nnn равна:- {sum_string}")