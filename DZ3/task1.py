# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

N = int(input('Введите число N первых элементов последовательности Фибоначчи: '))
fib = []
for i in range(N):
    if i == 0 or i == 1:
        fib.append(1)
    else:
        fib.append(fib[i - 1] + fib[i - 2]) 
print(*fib)

