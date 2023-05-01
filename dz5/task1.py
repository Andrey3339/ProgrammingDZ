# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5.
# Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

from random import randint

n = int(input('Введите количество чисел в списке: '))
ls = [str(randint(1, 10)) for i in range(n)]
print(", ".join(ls), end=' -> ')
print(", ".join(list(filter(lambda x: int(x) > 5, ls))))