# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def power_rec(a, b):
    if a == 0:
        return 0
    if b == 0 or a == 1:
        return 1
    return a*power_rec(a, b-1)


print("\nВведите A и B через пробел: ")
pow = [int(i) for i in input().split()][:2]
print(f'{pow[0]} в степени {pow[1]} равно: {power_rec(pow[0],pow[1])}')


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

def sum_rec(a, b):
    if b == 0:
        return a
    if b == 1:
        return a + 1
    return 1 + sum_rec(a, b-1)


print("Введите A и B через пробел: ")
pow = [int(i) for i in input().split()][:2]
print(f'{pow[0]} + {pow[1]} = {sum_rec(pow[0],pow[1])}')
