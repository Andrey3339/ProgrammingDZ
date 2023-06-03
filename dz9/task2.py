# Задача 2. Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.

import numpy as np

matrix_size = (5, 5)

# создаем матрицу из 0 и 1 размером size
matrix = np.random.randint(0, 2, matrix_size)
print()
print(matrix)

# флаг наличия одинаковых строк
match_flag = False
for row_count in range(matrix.shape[0]):        
    # вычитаем из матрицы каждую строку матрицы 
    matrix_row_diff = matrix - matrix[row_count]

    # получаем инвертированный список наличия ненулевых элементов в каждой строке
    inverted_list_no_zero_elements = ~matrix_row_diff.any(axis=1)
    
    # получаем список элементов и список количества этих элементов
    list_unique_elements, list_number_unique_elements = np.unique(inverted_list_no_zero_elements, return_counts=True)

    # создаем словарь 
    dictionary_number_unique_elements = dict(zip(list_unique_elements, list_number_unique_elements))
    
    # если нулевых строк больше 1, значит есть одинаковые строки
    if dictionary_number_unique_elements[True] > 1:        
        match_flag = True

if match_flag == True:
    print('\nВ матрице есть одинаковые строки')
else:
    print('\nВ матрице нет одинаковых строк')



