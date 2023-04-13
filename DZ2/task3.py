# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2


def dz3():
    substring = input('Введите подстроку, символы которой будем искать во фразе: ')
    phrase = input('Введите фразу: ')
    ls = len(substring)
    lph = len(phrase)
    dict = {}
    for x in range(ls):
        dict[substring[x]] = 0
    for i in range(ls):
        for j in range(lph):
            if substring[i] == phrase[j]:
                dict[substring[i]] = dict[substring[i]] + 1
                
    print(f'Во фразе {phrase} символы подстроки {substring} встречаются таким образом: \n{dict}')

dz3()