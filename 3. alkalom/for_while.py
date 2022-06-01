# ciklusok

# while ciklus - hátultesztelős ciklus
# for ciklus - elöltesztelős ciklus - foreach

# while ciklus

# akkor használunk általában, amikor 
# event szerű működésünk van: videójáték

"""
while logikai kifejezés:
    fut fut fut
    logikai_kifejezés léptetése
"""

num = 10

while num > 0:
    #print(f"{num}")
    num -= 1
    # num = num - 1

# for ciklus: valamilyen iterálható objektumon szeretnénk végig menni 
# lista, tuple, dictionary, set, queue, generator object összefoglaló neve: iterable object 
# iterálható objektum pl: lista, tuple, dictionary stb.

"""
for ciklus_változó in iterálható_object:
    programkód
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

temp_list = []

for item in my_list:    
    if (item%2) != 0:
        temp_list.append(item)

#print(temp_list)

my_list = [2, 4, 6, 3, 10, 2, 5, 6, 8]

my_idx = -1
max_val = 0
idx_value = 0

for item in my_list:
    my_idx += 1 
    if item > max_val:
        max_val = item
        idx_value = my_idx

#print(f"max: {max_val}, idx: {idx_value}")
#a = b = c = d = 10

# unpacking
# a, b = (10, 11)

# a, *b = (10, 11, 12)

# a, *b = [10, 11, 12]

# print(a)
# print(b)



# for idx, item in enumerate(my_list):
#     print(f"{idx} - {item}")


my_list = ['1', 1, 2, "2", 3, "3", '1', 1, 2, "2", 3, "3", '1', 1, 2, "2", 3, "3"]

for item in my_list:
    pass

# break: megállítja és kilép ciklus futásából
# continue: a következő iterációra ugrik
num = 0
for item in my_list:
    if type(item) == str:
        continue
    else:
        num += item

num = 0
for item in my_list:
    if type(item) == str:
        break
    else:
        num += item

#print("van élet a break után")

my_dict = {
    "name":[{'kulcs': "érték"}],
    "age": 32
}


for key, value in my_dict.items():
    print(key, value)
    if type(value) == list:
        for item in value:
            print(item)
            for k, v in item.items():
                print(k, v)

print("#######################################")
#############################################################

# for i in range(1, 1000, 20):
#     print("Okos vagyok")


my_list = [1, 2, 3]

my_range = range(3)

print(my_range)
print(my_list)

print(type(my_range))

print(len(my_list))
print(len(my_range))

print(my_list[0])
print(my_range[0])


# comprehension
#feladatok gyakorlása

# elkezdjük a függvényeket megismerni