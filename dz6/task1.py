# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN 
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

N = input('Введите натуральное число N: ')
print(f'Полученне число = {N} + {N + N} + {N + N + N} = {int(N) + int(N + N) + int(N + N + N)}')
