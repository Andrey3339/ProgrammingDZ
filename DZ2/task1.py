# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def subdz1(n):
    i = 1
    fk = 1
    while i <= n:
        fk *= i
        i += 1
    return fk

def dz1():
    N = int(input('Введите число N: '))
    i = 1
    while i <= N:
        print(subdz1(i), end=' ')
        i += 1
dz1()