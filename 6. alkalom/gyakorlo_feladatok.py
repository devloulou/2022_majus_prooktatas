# 1. feladat: Írjatok egy olyan függvényt, ami az alább megadott 2 dictionaryből egy harmadikat készít - merge-li őket -

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

def merge_dict():
    return dict1 | dict2

def merge_dict():
    return {**dict1, **dict2}

#print(merge_dict())

############################################################################
# 2. feladat: írjatok egy olyan függvényt, amely az alábbi dictionary-ben,
# az értékek közzül csak azokat hagyja meg,
# amelyek semelyik másik listában nem szerepel

# Példa:
# test_dict = {'ricsi': [1], 'norbi': [1,2,3]}
# my_func(test_dict)
# output: {'ricsi': [], 'norbi': [2,3]}
#

test_dict = {'Jolán' : [1, 4, 5, 6],
            'Ibolya' : [1, 8, 9],
            'Jácint': [10, 22, 4],
            'Karcsi': [5, 11, 22]}

# 1. feladat:  

[[1, 4, 5, 6], [1, 8, 9], [10, 22, 4], [5, 11, 22]]

def my_func():
    ret_val = {}
    cnt = -1
    for key, value in test_dict.items():
        cnt += 1
        temp = []
        for idx, item in enumerate(list(test_dict.values())):
            if cnt == idx:
                continue

            set_val = set(value)
            set_item = set(item)

            num = set_val.intersection(set_item)

            if len(num) > 0:
                temp.append(list(num)[0])

        ret_val[key] = [item for item in value if item not in temp]

            # for i in value:
            #     if i not in item:
            #         temp.append(i)
    return ret_val

ret_val = my_func()

#print(ret_val)

my_dict = {}

my_dict.update({'key': 'value'})

my_dict['kulcs'] = "érték"

#print(my_dict)
####################################################################################

# 3. feladat: írjatok egy olyan függvényt, amely az alábbi példában látható módon alakítka át:

# test_list = [{'tibi': 10, 'fizetes': 123 }, {'tibi': 5, 'fizetes': 456 }]
# my_func(test_list)
# output: [['tibi', 'fizetes'], [10, 123], [5, 456]]

test_list = [{'Robi' : 17, 'Karcsi' : 18, 'Vendel' : 20},
             {'Robi' : 21, 'Karcsi' : 30, 'Vendel' : 10},
             {'Robi' : 31, 'Karcsi' : 12, 'Vendel' : 19}]

def my_func():
    keys = []
    values = []
    for item in test_list:
        keys = list(item.keys())
        values.append(list(item.values()))

    return [keys, *values]
   


#print(my_func())


# 4. feladat: az alábbi lista elemeit alakítsuk át a példában megadott módon


test_list = [('Robi', 17), ('Karcsi',18) , ('Vendel', 20)]

# elvárt output: [{'Robi' : 17}, {'Karcsi' : 18}, {'Vendel' : 20}]

def my_func():
    my_list = []
    for item in test_list:
        my_dict = {item[0]: item[1]}
        my_list.append(my_dict)

    return my_list

print(my_func())