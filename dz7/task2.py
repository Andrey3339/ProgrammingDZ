# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.

# оборачиваем еще в одну функцию для передачи параметров (количество повторений)
def repeat_function(n):
    # сюда передается сама функция, которую мы декорируем (этой функцией оборачиваем целевую функцию)
    def our_func(func):
        # здесь определяется логика декоратора
        def decorator():
            for _ in range(n):
                func()
        return decorator
    return our_func


# декоратор измерения времени выполнения
def stopwatch(func):
    import time
    def decorator():
          start_time = time.time()
          func()
          stop_time = time.time()
          print(f'время выполнения: {stop_time - start_time}')
    return decorator

@stopwatch # затем декорируем на измерение времени выполнения заданного количества раз в предыдущем декораторе
@repeat_function(1000) # так декорируется функция our_func() - сначала задаем количество выполнений
def our_func():
    print('Привет!!!')

our_func()

