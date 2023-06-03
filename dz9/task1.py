# Задача 1. Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import numpy as np

list_size = 20

item_list = np.random.randint(1, 100, list_size)

print(f'\nСписок элементов: {item_list}')

unique_element = np.unique(item_list)

print(f'\nУникальные элементы списка: {unique_element}')

print(f'\nКоличество уникальных элементов: {len(unique_element)}\n')



