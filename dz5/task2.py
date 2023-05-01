# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа,
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.
from random import randint
n = 10
ls = [int((randint(1, 10))) for i in range(n)]
print(ls)
print()
lsup = []
fl = 1
for j in range(n):
    temp1 = ls[j]
    if j < n - 1:
        temp2 = ls[j + 1]

    lsup.append(ls[j])
    for i in range(j + 2, n):
        if (temp1 < temp2) and (temp2 < ls[i]):
            lsup.append(temp2)
            lsup.append(ls[i])
            temp1 = temp2
    if len(lsup) > 1:
        print(lsup)
    lsup = []



#print(list(filter(lambda , ls)))        
#from functools import reduce

#lst = [1, 5, 2, 3, 4, 6, 1, 7]

# from functools import reduce
# items = [1, 24, 17, 14, 9, 32, 2]
# all_max = reduce(lambda a, b: a if (a > b) else b, items)
# print(all_max)

#from functools import reduce

#ls = [1, 5, 2, 3, 4, 6, 1, 7]

# res = reduce(lambda acc, x: acc + [x] if x > acc[-1] else acc[:-1] + [x] if len(acc) > 1 and x > acc[-2] else [x], ls[1:], [ls[0]])
# #res = reduce(lambda acc, x: acc + [x] if x > acc[-1] else acc[:-1] + [x], ls[1:], [ls[0]])
# result = [ls[0]]
# i = 1
# while len(result) == 1 and i <= len(result):
#     #result = reduce(lambda acc, x: acc + [x] if x > acc[-i] else acc[:-1] + [x] if len(acc) > 1 and x > acc[-2] else [x], ls[i:], [ls[i - 1]])
#     result = [ls[i - 1]]
#     for x in ls[i:]:
#         if x > result[-i]:
#             result.append(x)
#         elif len(result) > 1 and x > result[-2]:
#             result[-1] = x
#     i += 1


#print(result)

# data = [i * j for i in range(1, 3) for j in range(3, 5)]
# print(data)

# data = []
# for i in range(1, 3):
#     for j in range(3, 5):
#         data.append(i * j)
# print(data)


#print(res)