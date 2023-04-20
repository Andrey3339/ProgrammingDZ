# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 3x^2 + x + 8
# 3. Результат: 8x^2 + 4x + 8

def sp(ls):
    s = str(*ls).split()
    dsp = {}
    if len(s) == 5:
        dsp = len5(s)
    if len(s) == 3:
        dsp = len3(s)
    if len(s) == 1:
        dsp = len1(s)
    return dsp

def len1(s):
    d3 = {}
    if 'x^2' in str(s):
        if s[0].replace('x^2', '') == '':
            d3['x^2'] = 1
        elif s[0].replace('x^2', '') == '-':
            d3['x^2'] = -1
        else:
            d3['x^2'] = int(s[0].replace('x^2', ''))
    elif 'x' in str(s) and 'x^2' not in str(s):
        if s[0].replace('x', '') == '':
            d3['x'] = 1
        elif s[0].replace('x', '') == '-':
            d3['x'] = -1
        else:
            d3['x'] = int(s[0].replace('x', ''))
    else:
        d3['c'] = int(s[0])
    return d3

def len3(s):
    d2 = {}
    if str(s).count('x') == 2:
        if s[0].replace('x^2', '') == '':
            d2['x^2'] = 1
        elif s[0].replace('x^2', '') == '-':
            d2['x^2'] = -1
        else:
            d2['x^2'] = int(s[0].replace('x^2', ''))
        if s[1] == '+':
            if s[2].replace('x', '') == '':
                d2['x'] = 1
            else:
                d2['x'] = int(s[2].replace('x', ''))
        if s[1] == '-':
            if s[2].replace('x', '') == '':
                d2['x'] = -1
            else:
                d2['x'] = -int(s[2].replace('x', ''))
    if str(s).count('x') == 1:
        if 'x^2' in str(s):
            if s[0].replace('x^2', '') == '':
                d2['x^2'] = 1
            elif s[0].replace('x^2', '') == '-':
                d2['x^2'] = -1
            else:
                d2['x^2'] = int(s[0].replace('x^2', ''))
            if s[1] == '+':
                d2['c'] = int(s[2])
            if s[1] == '-':
                d2['c'] = -int(s[2])
        else:
            if s[0].replace('x', '') == '':
                d2['x'] = 1
            elif s[0].replace('x', '') == '-':
                d2['x'] = -1
            else:
                d2['x'] = int(s[0].replace('x', ''))
            if s[1] == '+':
                d2['c'] = int(s[2])
            if s[1] == '-':
                d2['c'] = -int(s[2])
    return d2

def len5(s):
    d1 = {}
    if s[0].replace('x^2', '') == '':
        d1['x^2'] = 1
    elif s[0].replace('x^2', '') == '-':
        d1['x^2'] = -1
    else:
        d1['x^2'] = int(s[0].replace('x^2', ''))
    if s[1] == '+':
        if s[2].replace('x', '') == '':
            d1['x'] = 1
        else:
            d1['x'] = int(s[2].replace('x', ''))
    if s[1] == '-':
        if s[2].replace('x', '') == '':
            d1['x'] = -1
        else:
            d1['x'] = -int(s[2].replace('x', ''))
    if s[3] == '+':
        d1['c'] = int(s[4])
    if s[3] == '-':
        d1['c'] = -int(s[4])
    return d1

def sm(d1, d2):
    dsm = {}
    if ('x^2' in d1.keys()) and ('x^2' in d2.keys()):
        if d1['x^2'] + d2['x^2'] != 0:
            dsm['x^2'] = d1['x^2'] + d2['x^2']
    elif 'x^2' in d1.keys():
        dsm['x^2'] = d1['x^2']
    elif 'x^2' in d2.keys():
        dsm['x^2'] = d2['x^2']
    if ('x' in d1.keys()) and ('x' in d2.keys()):
        dsm['x'] = d1['x'] + d2['x']
    elif 'x' in d1.keys():
        dsm['x'] = d1['x']
    elif 'x' in d2.keys():
        dsm['x'] = d2['x']
    if ('c' in d1.keys()) and ('c' in d2.keys()):
        dsm['c'] = d1['c'] + d2['c']
    elif 'c' in d1.keys():
        dsm['c'] = d1['c']
    elif 'c' in d2.keys():
        dsm['c'] = d2['c']
    return dsm

def df(d1, d2):
    ddf = {}
    if ('x^2' in d1.keys()) and ('x^2' in d2.keys()):
        if d1['x^2'] - d2['x^2'] != 0:
            ddf['x^2'] = d1['x^2'] - d2['x^2']
    elif 'x^2' in d1.keys():
        ddf['x^2'] = d1['x^2']
    elif 'x^2' in d2.keys():
        ddf['x^2'] = -d2['x^2']
    if ('x' in d1.keys()) and ('x' in d2.keys()):
        if d1['x'] - d2['x'] != 0:
            ddf['x'] = d1['x'] - d2['x']
    elif 'x' in d1.keys():
        ddf['x'] = d1['x']
    elif 'x' in d2.keys():
        ddf['x'] = -d2['x']
    if ('c' in d1.keys()) and ('c' in d2.keys()):
        ddf['c'] = d1['c'] - d2['c']
    elif 'c' in d1.keys():
        ddf['c'] = d1['c']
    elif 'c' in d2.keys():
        ddf['c'] = -d2['c']
    return ddf

def dict_to_str(d):
    sd = ''
    if 'x^2' in d.keys():
        if d['x^2'] == 1:
            sd = 'x^2'
        elif d['x^2'] == -1:
            sd = '-x^2'
        else:
            sd = str(d['x^2']) + 'x^2'
    if 'x' in d.keys() and 'x^2' in d.keys():
        if d['x'] > 0:
            if d['x'] == 1:
                sd += ' + x'
            else:
                sd += ' + ' + str(d['x']) + 'x'
        else:
            if d['x'] == -1:
                sd += ' - x'
            else:
                sd += ' - ' + str(-d['x']) + 'x'
    if 'x' in d.keys() and 'x^2' not in d.keys():
        if d['x'] > 0:
            if d['x'] == 1:
                sd += 'x'
            else:
                sd += str(d['x']) + 'x'
        else:
            if d['x'] == -1:
                sd += ' -x'
            else:
                sd += '-' + str(-d['x']) + 'x'
    
    if 'c' in d.keys() and ('x^2' in d.keys() or 'x' in d.keys()):
        if d['c'] > 0:
            sd += ' + ' + str(d['c'])
        else:
            sd += ' - ' + str(-d['c'])
    if 'c' in d.keys() and ('x^2' not in d.keys() and 'x' not in d.keys()):
        if d['c'] > 0:
            sd += str(d['c'])
        else:
            sd += '-' + str(-d['c'])
    return sd

dtmn1 = open('mn1.txt', "r", encoding='utf-8')
tmn1 = dtmn1.readlines()
dtmn2 = open('mn2.txt', "r", encoding='utf-8')
tmn2 = dtmn2.readlines()
dtmn3 = open('mn3.txt', "r", encoding='utf-8')
tmn3 = dtmn3.readlines()
dtmn4 = open('mn4.txt', "r", encoding='utf-8')
tmn4 = dtmn4.readlines()
dtmn5 = open('mn5.txt', "r", encoding='utf-8')
tmn5 = dtmn5.readlines()
dtmn6 = open('mn6.txt', "r", encoding='utf-8')
tmn6 = dtmn6.readlines()
dtmn7 = open('mn7.txt', "r", encoding='utf-8')
tmn7 = dtmn7.readlines()

print()

d1d2sm = sm(sp(tmn1), sp(tmn2))
print(f"Сумма многочленов {str(tmn1)} и {str(tmn2)} равна ['{dict_to_str(d1d2sm)}']")

d1d2sm = sm(sp(tmn2), sp(tmn3))
print(f"Сумма многочленов {str(tmn2)} и {str(tmn3)} равна ['{dict_to_str(d1d2sm)}']")

d1d2sm = sm(sp(tmn2), sp(tmn4))
print(f"Сумма многочленов {str(tmn2)} и {str(tmn4)} равна ['{dict_to_str(d1d2sm)}']")

d1d2sm = sm(sp(tmn2), sp(tmn5))
print(f"Сумма многочленов {str(tmn2)} и {str(tmn5)} равна ['{dict_to_str(d1d2sm)}']")

d1d2sm = sm(sp(tmn1), sp(tmn6))
print(f"Сумма многочленов {str(tmn1)} и {str(tmn6)} равна ['{dict_to_str(d1d2sm)}']")

d1d2sm = sm(sp(tmn2), sp(tmn7))
print(f"Сумма многочленов {str(tmn2)} и {str(tmn7)} равна ['{dict_to_str(d1d2sm)}']")

d1d2sm = sm(sp(tmn1), sp(tmn7))
print(f"Сумма многочленов {str(tmn1)} и {str(tmn7)} равна ['{dict_to_str(d1d2sm)}']")

print()

d1d2df = df(sp(tmn1), sp(tmn2))
print(f"Разность многочленов {str(tmn1)} и {str(tmn2)} равна ['{dict_to_str(d1d2df)}']")

d1d2df = df(sp(tmn2), sp(tmn3))
print(f"Разность многочленов {str(tmn2)} и {str(tmn3)} равна ['{dict_to_str(d1d2df)}']")

d1d2df = df(sp(tmn2), sp(tmn4))
print(f"Разность многочленов {str(tmn2)} и {str(tmn4)} равна ['{dict_to_str(d1d2df)}']")

d1d2df = df(sp(tmn2), sp(tmn5))
print(f"Разность многочленов {str(tmn2)} и {str(tmn5)} равна ['{dict_to_str(d1d2df)}']")

d1d2df = df(sp(tmn1), sp(tmn6))
print(f"Разность многочленов {str(tmn1)} и {str(tmn6)} равна ['{dict_to_str(d1d2df)}']")

d1d2df = df(sp(tmn2), sp(tmn7))
print(f"Разность многочленов {str(tmn2)} и {str(tmn7)} равна ['{dict_to_str(d1d2df)}']")

d1d2df = df(sp(tmn1), sp(tmn7))
print(f"Разность многочленов {str(tmn1)} и {str(tmn7)} равна ['{dict_to_str(d1d2df)}']")

print()

dtmn1.close()
dtmn2.close()
dtmn3.close()
dtmn4.close()
dtmn5.close()
dtmn6.close()
dtmn7.close()




