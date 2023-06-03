# Задача 3. Создайте двумерный массив случайного размера. Найдите индексы 
# максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy as np

number_lines = np.random.randint(1, 10)
number_columns = np.random.randint(1, 10)

array_size = number_lines, number_columns

array_random_size = np.random.randint(1, 100, array_size)
print()
print(array_random_size)

max_array_element = np.argmax(array_random_size)
element_line_number = max_array_element // len(array_random_size[0])
element_column_number = max_array_element % len(array_random_size[0])
print(f'\nИндекс максимального элемента - {array_random_size[element_line_number][element_column_number]}, ', end='')
print(f'начиная с 0:  x = {element_line_number}, y = {element_column_number}')

min_array_element = np.argmin(array_random_size)
element_line_number = min_array_element // len(array_random_size[0])
element_column_number = min_array_element % len(array_random_size[0])
print(f'\nИндекс минимального элемента - {array_random_size[element_line_number][element_column_number]}, ', end='')
print(f'начиная с 0:  x = {element_line_number}, y = {element_column_number}')

print(f'\nЭлементы главной диагонали матрицы:  {np.diag(array_random_size)}\n')

