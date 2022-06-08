# 1. feladat
# Írjatok egy olyan scriptet, amely
# kiírja a megadott lista index-eit és elemeit

# pl: 0 - 10
# 1 - 20

my_list = [10, 20, 30, 40, 50, 60, 70]

# my_enumerate = enumerate(my_list)
# my_enumerate = enumerate

# for item in my_enumerate(my_list):
#     print(item)

# for item in enumerate(my_list):
#     print(f"{item[0]} - {item[1]}")

# cnt = -1
# for item in my_list:
#     cnt += 1
#     print(f"{cnt} - {item}")

# 2. feladat:
# töröljétek ki azt az elemet, ahol nem szerepel író

my_dict = {
    "books": [
        {
            "writer": "J.K. Rowlings",
            "book": "Harry Potter and the Goblet of the Fire"
        },
        {            
            "book": "Sorstalanság"
        },
        {
            "writer": "Mikszáth Kálmán",
            "book": "Szent Péter esernyője"
        },
        {            
            "book": "Sorstalanság",
            "writer": ""
        }
    ]

}

#my_dict['books'].pop(1)

for item in my_dict['books']:
    # print(not item.get('writer'), item.get('writer'))
    if not item.get('writer'):
        my_dict['books'].remove(item)
    # # else:
    #     if len(item['writer']) == 0:
    #         my_dict['books'].remove(item)

# print(my_dict)

# 3. feladat:
# gyűjtsétek ki egy listába a megadott dictionary kulcsait
# használjatok dictionary-hez kapcsolódó művelete / függvényt


my_dict = {
    "foo": "bar",
    "color": "blue",
    "country": "Sweden"
}

my_list = list(my_dict.keys())

# 4. feladat:
# töröljétek az összes olyan elemet a listából, amely
# nem osztható maradék nélkül 3-al

my_list = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
#          0  1  2  3   4   5   6   7   8   9   10  11
# for idx, item in enumerate(my_list):
#     if item%3!=0:
#         my_list.pop(idx)

# print(my_list)

# my_list2 = []

# for item in my_list:
#     if item%3==0:
#         my_list2.append(item)

# print(my_list2)

# 5. feladat:
# írjatok egy olyan programot, amely a 2 listából csinál egy dictionary-t
# pl: {
#   1: "alma",
#   2: "körte"
#   .
#   .
#   5: "dinnye"
# }

my_list = [1, 2, 3, "Józsi", 5]
my_list2 = ["alma", "körte", "barack", "banán"]

my_dict = {}

for idx, item in enumerate(my_list):
    if len(my_list2) - 1 >= idx:
        my_dict[item] = my_list2[idx]

print(my_dict)

my_dict = dict(zip(my_list, my_list2))
print(my_dict)

###################################
exit()
for item in zip(my_list, my_list2):
    print(item)

#print(my_dict)