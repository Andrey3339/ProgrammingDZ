# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.


def dz2():
    print(f'x | y | z | -(x ∧ y) ∨ Z')
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f'{x} | {y} | {z} |  {int(not(x and y) or z)}')

dz2()