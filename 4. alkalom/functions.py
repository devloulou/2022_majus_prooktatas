"""
def függvény_neve(opcionális_paraméterlista):
    utasítások

print()

"""

from decimal import DivisionByZero


def my_func(a, b):
    return a + b

my_val = my_func(1, 2)

# print(my_func(1, 2))
# print(my_val)

def my_func(a=1, b=2):
    return a + b

# ennél a megoldásnál pozíció alapon történik az érték adás
my_val = my_func(5)

my_val = my_func(b=10)
my_val = my_func(10, 12)
my_val = my_func(a=10, b=20)

#print(my_val)

def my_func():
    print("semmi")

#print(my_func())

########################################

# packing és unpacking függvények esetében

# *args, **kwargs

def my_func(*args):
    #print(args)
    return 

my_func(1)
my_func(1,2)
my_func(1, 10, 20)
my_func(1, "Ricsi", "Feri")
my_func(1, *[1, 2, 3, 4])


def my_func(**kwargs):
    #print(kwargs)
    return

my_func(name="Ricsi", age=32, autos=['BMW', 'VOLVO'])

## **kwargs

def my_func(*args, **kwargs):
    # print(args)
    # print(kwargs)
    return

#my_func(1, "Ricsi", "Feri")
my_func(name="Ricsi", age=32, autos=['BMW', 'VOLVO'])

my_func(1, 2, 3, 10, name="Ricsi" )

###########################


def calculator(num1, num2, operation):    
    def _add():
        return num1 + num2

    def _minus():
        return num1 - num2

    def _multiple():
        return num1 * num2

    def _divison():
        return num1 / num2

    if operation == '+':
        return _add()
    
    elif operation == '-':
        return _minus()
    
    elif operation == '*':
        return _multiple()

    elif operation == '/':
        return _divison()

#print(calculator(1, 0, '/'))

########### hibakezelés

"""
teljes hibakezelő blokk -> a finally az opcionális
több except ágad is lehet

try:
    utasítás
except:
    ha hiba van, utasítás
finally:
    ez minden esetben le fog futni (ha nincs futási idejű hiba)


"""

# num1 = 10
# num2 = 10

# if num1 > num2:
#     print()
# elif num2 > num1:
#     raise Exception(" ez egy futási dejű hiba")

# elif num1 == num2:
#     raise ZeroDivisionError(" A két szám egyenlő")

num1 = 1
num2 = 0

# try:
#     my_val = num1 / num2
#     print(my_val)
# except ZeroDivisionError:
#     print("ide futottam")
# except Exception as error:
#     print(error)


num1 = 100
num2 = 150

# try:
#     if 0 > (num1 - num2):
#         raise Exception("Nincs pénzed")
#     else:
#         print("ok")
# except Exception as e:
#     print(e)

# print("megy tovább a futás")

####################################

# my_num = 0

# try:
#     if my_num > 0:
#         print("azta")
#     else:
#         raise Exception(f"{my_num} is not bigger")
# except Exception as e:
#     print(e)

# finally:
#     print("Lefutott a finally")

def calculator(num1, num2, operation):    
    def _add():
        return num1 + num2

    def _minus():
        return num1 - num2

    def _multiple():
        return num1 * num2

    def _divison():
        return num1 / num2

    if operation == '+':
        return _add()
    
    elif operation == '-':
        return _minus()
    
    elif operation == '*':
        return _multiple()

    elif operation == '/':
        # if num2 == 0:
        #     return False, "második szám 0"
        try:
            return _divison()
        except Exception as e:
            return str(e)

print(calculator(1, 1, '/'))


# generátor függvények
# decorator függvények
# modulok és package