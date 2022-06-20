import os

my_string = "valami/valami2/ricsi"

print(__file__)
print(os.path.basename(__file__))

print(os.path.dirname(my_string))
print(os.path.dirname(__file__))

print(os.listdir())
print(os.listdir('.'))

print(os.listdir(os.path.dirname(__file__)))
print("----------------------------")
my_dir = os.path.dirname(__file__)
my_file = os.path.basename(__file__)

print(my_dir)
print(my_file)

print(os.path.join(my_dir, my_file))

num1 = '3'
num2 = "4"

print(os.path.join(num1, num2))


####################################################