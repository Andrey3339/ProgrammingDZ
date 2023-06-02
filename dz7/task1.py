# Задача 1. Создайте пользовательский аналог метода map().

def our_map(function, iterated_object):
    return [function(i) for i in iterated_object]

# пример применения:

our_list = [2, 4, 8, 9, 2, 3, 5, 7, 1]

print(list(our_map(lambda x: x ** 2, our_list)))

print(list(map(lambda x: x ** 2, our_list)))

# результат одинаковый

