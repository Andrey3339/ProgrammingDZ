# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PVeAPgUhodEEqzW53E9wk1RwnoR2PYqS

Задача 1. Найдите, какая область центрального федерального округа имела наибольшую численность студентов вечерней формы обучения в 2015 году.
"""

import pandas as pd

df = pd.read_csv('sample_data/data2015_2019.csv', sep=';', encoding='cp1251')

# оставляем только области в ЦФО (исключая г. Москва), так как в задании ...какая область....
df_2015 = df.iloc[ 2 : 19, : ]
#df_2015

# находим максимальное значение студентов вечерней формы обучения в 2015 г
max_value = df_2015['Численность студентов очно-заочная (вечерняя) форма, человек, 2015'].max()
# делаем отбор по max_value
df_2015 = df_2015[df_2015['Численность студентов очно-заочная (вечерняя) форма, человек, 2015'] == max_value]

# выводим толко 2 кнужные колонки
df_2015 = pd.DataFrame(df_2015, columns=['Субъект РФ', 'Численность студентов очно-заочная (вечерняя) форма, человек, 2015'])
df_2015

"""Задача 2. Постройте диаграмму с данными о численности студентов дневной формы обучения южного федерального округа за 2017 год."""

import seaborn as sns

# оставляем только регионы ЮФО
df_2017 = df.iloc[ 33 : 41 , : ]

# строим диаграмму зависимости численности студентов дневной формы обучения южного федерального округа за 2017 год от региона ЮФО
plot = sns.barplot(df_2017, x = 'Субъект РФ', y = 'Численность студентов, очная форма, человек, 2017')
# поворачиваем данные из колонки 'Субъект РФ' на 90 градусов
plot.set_xticklabels(labels = df_2017['Субъект РФ'], rotation = 90)

"""Задача 3. Постройте диаграмму количества студентов заочной формы обучения за 2019 год по всем регионам, в которых общее количество студентов не превышает 10000 за данный год."""

# делаем отбор общего количества студентов не превышающего 10000 за 2019 по всем регионам
df_2019 = df[df['Численность студентов, всего человек, 2019'] <= 10000]
# на основе полученно отбора строим диаграмму зависимости количества студентов заочной формы обучения за 2019 год от региона
plot = sns.barplot(df_2019, x = 'Субъект РФ', y = 'Численность студентов заочная форма, человек, 2019')
# поворачиваем данные из колонки 'Субъект РФ' на 90 градусов
plot.set_xticklabels(labels = df_2019['Субъект РФ'], rotation = 90)