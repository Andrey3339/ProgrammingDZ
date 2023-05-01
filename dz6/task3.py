# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

# простая несократимая дробь - когда наибольший (и единственный) общий делитель числителя и знаменателя равен 1
# Разложим числитель и знаменатель на простые множители и найдем их наибольший общий делитель. 
# Если он равен 1, дробь несократима.

# (0, 1/11, 2/11, 3/11, 4/11, 5/11, 6/11, 7/11, 8/11, 9/11, 10/11, 1)
# (0, 1/10, 2/10, 3/10, 4/10, 5/10, 6/10, 7/10, 8/10, 9/10, 1)
# .........
# (0, 1/3, 2/3)
# (0, 1/2, 1)
N = int(input('Введите максимальный знаменатель:  '))
n = N
dsn = {}
ds = []
mulls = []
result = []
# ищем все простые множители от 2 до введенного числа и возвращаем их в виде списка

def find_simple_mult(N):
    divl = []
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if( i % j == 0):
                divl.append(j)
        if (len(divl) == 2):
            ds.append(i)
        divl = []
    return ds

# раскладываем число на простые множители 
def decomp_simple_mult(ds, N):
    n = N
    mul = []
    for i in ds:
        while n % i == 0:
            mul.append(i)
            n = n / i
        if N / i == 1:
            break
    return mul

ds = find_simple_mult(N)
mulls = decomp_simple_mult(ds, N)
dcls = []
dzls = []
for i in range(N, 1, -1):
    ds1 = find_simple_mult(N)
    dzls = set(decomp_simple_mult(ds1, i))
    for j in range(1, i):
        ds2 = find_simple_mult(N)
        dcls = set(decomp_simple_mult(ds2, j))
        if len(dzls.intersection(dcls)) == 0:
            print(f'{j}/{i}', end=' ')

