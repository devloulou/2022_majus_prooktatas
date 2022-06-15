# Generátor függvények

# lazy evaluation - "laza" kiértékelést
# meg tudod állítani a függvénye futását és képes vagy arra,
# hogy folytatni tudd

# yield 

def my_func():
    return 1
    return 2
    return 3

# 1 generátor függvényben több yield utasítás is lehet

def my_gen():
    print("yield 1 előtt")
    yield ['almafa', "barack"]
    print("yield 2 előtt")
    yield 2
    print("yield 3 előtt")
    yield 3
    print("yield 3 után")
    

func = my_gen()

# print(next(func))
# print(next(func))
# print(next(func))

# for item in func:
#     print("futok")
#     print(item)

# print(next(my_gen()))
# print(next(my_gen()))

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

#fnc = countdown(20)

for item in countdown(20):
    print(item)



