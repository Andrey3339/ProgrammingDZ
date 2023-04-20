# Задача 2. В первом списке находится информация об ассортименте мороженного, 
# во втором списке - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.

# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»

all_assort = {'Сливочное', 'Бурёнка', 'Вафелька', 'Сладкоежка', 'Пломбир', 'Шоколадное'}
in_stock = {'Сливочное', 'Вафелька', 'Сладкоежка'}

s = ', '.join(all_assort.difference(in_stock))
print('Закончилось:', s)

