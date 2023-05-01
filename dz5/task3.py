# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего 
# совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
#Список уникальных элементов [1, 4, 2, 3, 6, 7]

from random import randint
#from collections import Counter

n = int(input('Введите количество чисел в списке: '))
ls = [randint(1, 10) for i in range(n)]
print('Исследуемый список чисел:')
print(ls)

# делает словарь, где ключ это элемент списка, а значение - сколько раз этот элемент встречается в списке
lsnotd = {i : ls.count(i) for i in ls}
#print(lsnotd)

# можно так
#lsnotd2 = dict(Counter(ls))
#print(lsnotd2)

print('Список уникальных чисел:')
lsu = dict(filter(lambda item : item[1] == 1, lsnotd.items()))
print(list(lsu.keys()))

print('Список повторяющихся чисел:')
lsd = dict(filter(lambda item : item[1] != 1, lsnotd.items()))
print(list(lsd.keys()))