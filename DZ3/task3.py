# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему 
# неизвестна, он выводит соответствующую фразу.

def botv1(): # новые повросы и ответы повторяются только после перезагрузки бота
    datar = open('test.txt', "r", encoding='utf-8')
    text = datar.readlines()
    datar.close()
    d = {}
    dnew = {}
    for s in text:
        k, v = s.split(':')
        d[k] = v
    print('привет, я бот задайте свой вопрос(для выхода введите 0): ')
    # моржовый оператор
    while q := input('-->  '):
        if q == "0":
            break
        if q in d.keys():
            print(d[q], end='')
        else:
            print('не понимаю я по-вашему нихера...')
            s1 = input(f'напиши ответ на свой вопрос:  {q}: ')
            dnew[q] = s1 + '\n'

    dataw = open('test.txt', "a", encoding='utf-8')
    for kw, vw in dnew.items():
        dataw.write(f'{kw}:{vw}')

    dataw.close()

#botv1()

def botv2():
    datarw = open('test.txt', "r+", encoding='utf-8')
    text = datarw.readlines()
    d = {}
    for s in text:
        k, v = s.split(':')
        d[k] = v
    print('привет, я бот задайте свой вопрос(для выхода введите 0): ')
    # моржовый оператор
    while q := input('-->  '):
        if q == "0":
            break
        if q in d.keys():
            print(d[q], end='')
        else:
            print('не понимаю я по-вашему нихера...')
            s1 = input(f'напиши ответ на свой вопрос:  {q}: ')
            d[q] = s1 + '\n'
            datarw.write(f'{q}:{d[q]}')
    datarw.close()

botv2()

