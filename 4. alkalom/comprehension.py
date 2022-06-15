# comprehension művelet

# list comprehension, dictionary comprehension, generator comprehension - generator kifejezés

my_list = []

for item in range(1000):
    if item%2== 0:
        my_list.append(item)

#print(my_list)

my_list = [item for item in range(1000) if item%2== 0]

#print(my_list)

my_list = [1, 2, 3, "Józsi", 5]
my_list2 = ["alma", "körte", "barack", "banán"]

my_dict = { item : my_list2[idx] for idx, item in enumerate(my_list) if len(my_list2) - 1 >= idx}

#print(my_dict)

########### 
# generator expression
import sys

my_list = [item for item in range(1000)]

my_gen = (item for item in range(10))

print(sys.getsizeof(my_list))
print(sys.getsizeof(my_gen))

exit()
for item in my_gen:
    print(item)

# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
#print(next(my_gen))

# lazy avaluation - "laza kiértékelés" ---- list comprehension nem lazy evaluation

