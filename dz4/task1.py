# Задача 1. Дано натуральное число N. Напишите метод, который вернёт список простых множителей
# числа N и количество этих множителей.

# 60 -> 2, 2, 3, 5

N = int(input('Введите натуральное число N:  '))
n = N
divl = []
dsn = {}
# ищем список простых множителей введенного числа
for i in range(1, int(N ** 0.5) + 1):
    for j in range(1, i + 1):
       if( i % j == 0):
            divl.append(j)
    if (len(divl) == 2):
        dsn[i] = divl
    divl = []

mulls = []
for i in dsn.keys():
    while n % i == 0:
        mulls.append(i)
        n = n / i
    if N / i == 1:
        break
print(f'{N} -> {mulls}')


