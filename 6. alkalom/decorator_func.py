# olyan függvények, amelyek egy meglévő függvényhez adnak hozzá
# plusz tulajdonságot anélkül, hogy az eredeti függvényen változtatna


def my_func():
    print("Hello world!")

def my_func2(func, name):
    func(f"{name}")

my_func = print

# my_func("Hello world, sokadik")

# my_func2(print, "Ricsi")



def my_func():
    print("Hello world!")

def start_end_decor(func):
    def wrapper():
        print("Start")
        func()
        print("Finished")
    return wrapper

test = start_end_decor(my_func)

#test()

@start_end_decor
def countdown():
    num = 10
    while num > 0:
        print(num)
        num -= 1

#countdown()


def start_end2(func):
    def wrapper(*args, **kwargs):
        print(f"Start {func.__name__} function")
        result = func(*args, **kwargs)
        print(f"End")
        return result
    return wrapper

@start_end2
def add_numbers(a):
    return a + 5

# print(add_numbers(2))

from time import time

def time_it(func):
    def wrapper(*args, **kwargs):
        ts = time()
        retval = func(*args, **kwargs)
        print(time() - ts)
        return retval
    return wrapper

@time_it
def generate_random_data(num):
    import random
    my_list = []
    for item in range(num):
        if item not in my_list:
            my_list.append(random.randint(1, num))

    return len(my_list)


# print(generate_random_data(100_000))
    
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(5)
def greet(name):
    print(f"Hello, {name}")

greet(name='Aranka')


# logolás
# futási idő mérés
# debug
# register
# lassítani a futáson
# caching
