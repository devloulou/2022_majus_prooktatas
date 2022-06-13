# 1. feladat
# Írjatok egy olyan scriptet, amely
# a megadott lista elemeit elosztja 10-el
# és egy listába letárolja az így kapott értéket

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

my_list2 = []
my_list3 = [int(item/10) for item in my_list]

for item in my_list:
    my_list2.append(int(item/10))

# print(my_list2)
# print(my_list3)


# 2. feladat:
# a megadott dictionary-ben javítsátok a name kulcsot title-re


my_dict = {
    "game": {
        "action": [
            {"title": "Call of Duty"},
            {"title": "Battlefield"},
            {"name": "Need for Speed"}
        ],
        "rpg": [
            {"title": "Oblivion"},
            {"title": "Dark Souls"}
        ],
        "arcade": [{"name": "Need for Speed"}]
    }
}

import pprint

# ezt majd megnézni
# for key, value in my_dict.items():
#     if type(value) == list:
#         for item in value:
#             pass
#     elif type(value) == dict:
#         for k, v in value.items():
#             if type(v) == list:
#                 for i in v:
#                     print(i)
#             elif type(v) == dict:
#                 for k2, v2 in v.items():
#                     if k2 == 'name':
#                         v.update({'title': v2})
#                         # v.pop('name')
#     else:
#         continue

#print(my_dict)

for key, value in my_dict['game'].items():
    for item in value:
        if item.get('name'):
            item.update({'title': item['name']})
            item.pop('name')

#pprint.pprint(my_dict, indent=4)




# 3. feladat:
# gyűjtsétek ki egy listába a megadott dictionary kulcsait, egy másik listába az ártékeket
# használjatok dictionary-hez kapcsolódó művelete / függvényt


my_dict = {
    "foo": "bar",
    "color": "blue",
    "country": "Sweden",
    "foo": "valami"
}


my_list = list(my_dict.keys())
my_vals = list(my_dict.values())

my_keys = []
my_val2 = []

for key, value in my_dict.items():
    my_keys.append(key)
    my_val2.append(value)

print(my_keys)
print(my_val2)


# 4. feladat:
# töröljétek az összes olyan elemet a listából, amely
# nem osztható maradék nélkül 5-al

my_list = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
temp = [item for item in my_list if item%5==0]

# for item in my_list:
#     if item%5==0:
#         temp.append(item)

my_list = temp
print(my_list)

# 5. feladat:
# írjatok egy olyan scriptet, amely a lista elemeiből
# csak az utolsó 3 karaktert hagyja meg

# elvárt output:
# ["rna", "lma", "ata", "ack", "émi"]

my_list = ['Barna', "alma", "Kata", "barack", "Noémi"]

# 1. végig iterálok a listán
# 2. slicelom az utolsó 3 karakterét az elemeknek
# 3. opcionális: vagy új listába teszem, vagy a meglévőt módosítom
temp = []
for idx, item in enumerate(my_list):
    temp.append(item[-3:])
    my_list[idx] = item[-3:]

print(temp)
print(my_list)

my_list = ['Barna', "alma", "Kata", "barack", "Noémi"]
my_list = [item[-3:] for item in my_list]

print(my_list)
###############################################################
