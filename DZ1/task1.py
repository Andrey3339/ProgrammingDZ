# Задача 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и выводит название этого дня недели.

# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

n = int(input('введите номер дня недели: '))
if n < 1 or n > 7:
    print('Нет такого дня')
else:
    if n == 1:
        print(f'{n} -> Понедельник')
    elif n == 2:
        print(f'{n} -> Вторник')
    elif n == 3:
        print(f'{n} -> Среда')
    elif n == 4:
        print(f'{n} -> Четверг')
    elif n == 5:
        print(f'{n} -> Пятница')    
    elif n == 6:
        print(f'{n} -> Суббота')            
    else:
        print(f'{n} -> Воскресенье')


