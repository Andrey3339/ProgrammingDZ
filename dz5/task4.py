#Задача 4*. (Необязательная). Создайте игру в крестики-нолики.

def win(field):
    if field[0][0] == field[0][1] == field[0][2] == 'x' or \
       field[1][0] == field[1][1] == field[1][2] == 'x' or \
       field[2][0] == field[2][1] == field[2][2] == 'x' or \
       field[0][0] == field[1][0] == field[2][0] == 'x' or \
       field[0][1] == field[1][1] == field[2][1] == 'x' or \
       field[0][2] == field[1][2] == field[2][2] == 'x' or \
       field[0][0] == field[1][1] == field[2][2] == 'x' or \
       field[2][0] == field[1][1] == field[0][2] == 'x':
        return 'x'
    elif field[0][0] == field[0][1] == field[0][2] == 'o' or \
       field[1][0] == field[1][1] == field[1][2] == 'o' or \
       field[2][0] == field[2][1] == field[2][2] == 'o' or \
       field[0][0] == field[1][0] == field[2][0] == 'o' or \
       field[0][1] == field[1][1] == field[2][1] == 'o' or \
       field[0][2] == field[1][2] == field[2][2] == 'o' or \
       field[0][0] == field[1][1] == field[2][2] == 'o' or \
       field[2][0] == field[1][1] == field[0][2] == 'o':
        return 'o'
    else:
        return 'game'   
field = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
print('', field[0],'\n', field[1], '\n', field[2])
fl = 0
i = 0
d = [1, 2, 3]
count = 0
x = None
y = None
while fl == 0 and count < 9:
    if i % 2 == 0:
        fl1 = 0
        fl2 = 0
        while fl1 == 0:
            try:
                x, y = input('Введите координаты Х - номер строки и столбца от 1 до 3:   ').split()
                x = int(x)
                y = int(y)
            except Exception:
                print('Внимательно при вводе координат...')
            if x in d and y in d:
                if field[x - 1][y - 1] == ' ':
                    field[int(x) - 1][int(y) - 1] = 'x'
                    print('', field[0],'\n', field[1], '\n', field[2])
                    fl1 = 1
                    count += 1
                    print(count)
                else:
                    print(f'На этом месте уже стоит {field[x - 1][y - 1].upper()} ')
            else:
                print('Неправильные координаты ')
    if i % 2 != 0:
        while fl2 == 0:
            try:
                x, y = input('ведите координаты O: - номер строки и столбца от 1 до 3:   ').split()
                x = int(x)
                y = int(y)
            except Exception:
                print('Внимательно при вводе координат...')
            if x in d and y in d:
                if field[x - 1][y - 1] == ' ':
                    field[int(x) - 1][int(y) - 1] = 'o'
                    print('', field[0],'\n', field[1], '\n', field[2])
                    fl2 = 1
                    count += 1
                    print(count)
                else:
                    print(f'На этом месте уже стоит {field[x - 1][y - 1].upper()} ')
            else:
                print('Неправильные координаты')
    i += 1
    if win(field) == 'x':
        print("Выиграли крестики!...")
        break
    if win(field) == 'o':
        print("Выиграли нолики!...")
        break
    
