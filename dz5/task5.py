# Задача 5*. (Необязательная). Двумерный массив размером 5х5 заполнен случайными нулями и единицами.
# Игрок может ходить только по полям, заполненным единицами. Проверьте, существует ли путь
# из точки [0, 0] в точку [4, 4] (эти поля требуется принудительно задать равными единице).
from random import randint
def way(x, y):
    #print(f'{x} ---- {y}')
    if x == 4 and y == 4:
        print('ура!!!! есть путь!!!')
        return 'yes'
    elif x < 4 or y < 4:
        if y < 4 and field[x][y + 1] == 1:
            #print(f'пошли по X {x} : {y + 1} -> {field[x][y + 1]}')
            way(x, y + 1)
            # if y > 1 and field[x][y - 1] == 1:
            #     print(f'пошли по X {x} : {y - 1} -> {field[x][y - 1]}')
            #     way(x, y - 1)
        if x < 4 and field[x + 1][y] == 1:
            #print(f'пошли по Y {x + 1} : {y} -> {field[x + 1][y]}')
            way(x + 1, y)
            # if x > 1 and field[x - 1][y] == 1:
            #     print(f'пошли по Y {x - 1} : {y} -> {field[x - 1][y]}')
            #     way(x - 1, y)     
        # elif y < 4 and field[x][y + 1] == 0:
        #     print('Похоже нет пути!1')
        # elif x < 4 and field[x + 1][y] == 0:
        #     print('Похоже нет пути!2')
        # else:
        #     print('похоже нет пути((((')
        #     return 'no'
    else:
        print('похоже нет пути((((')
        return 'no'
field = [ [1, 1, 1, 1, 1],
          [1, 0, 0, 0, 1], 
          [1, 0, 1, 1, 0],
          [1, 0, 0, 0, 1],
          [1, 1, 1, 1, 1] ]
# field = [ ['', '', '', '', ''],
#           ['', '', '', '', ''],
#           ['', '', '', '', ''],
#           ['', '', '', '', ''],
#           ['', '', '', '', ''] ]
# field = [ [1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1], 
#           [1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1] ]
# for i in range(5):
#     for j in range(5):
#         field[i][j] = randint(0,1)
# field[0][0] = 1
# field[4][4] = 1
print('', field[0],'\n', field[1], '\n', field[2], '\n', field[3], '\n', field[4])

#w = way(0, 0)
print(way(0, 0))
# if w == 'yes':
#     print('Путь есть!')
# else:
#     print('Нет пути!')

# if way(0, 0) == 'yes':
#     print('Путь есть!')
# elif way(0, 0) == 'no':
#     print('Нет пути!')

#print(way(0, 0))
#a = way(0, 0)
#print(a)
# if (ls[0] == 4 and ls[1] == 4):
#     print('путь есть')