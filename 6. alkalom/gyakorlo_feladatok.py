# 1. feladat: Írjatok egy olyan függvényt, ami az alább megadott 2 dictionaryből egy harmadikat készít - merge-li őket -

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

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

####################################################################################

# 3. feladat: írjatok egy olyan függvényt, amely az alábbi példában látható módon alakítka át:

# test_list = [{'tibi': 10, 'fizetes': 123 }, {'tibi': 5, 'fizetes': 456 }]
# my_func(test_list)
# output: [['tibi', 'fizetes'], [10, 123], [5, 456]]

test_list = [{'Robi' : 17, 'Karcsi' : 18, 'Vendel' : 20},
             {'Robi' : 21, 'Karcsi' : 30, 'Vendel' : 10},
             {'Robi' : 31, 'Karcsi' : 12, 'Vendel' : 19}]


# 4. feladat: az alábbi lista elemeit alakítsuk át a példában megadott módon


test_list = [('Robi', 17), ('Karcsi',18) , ('Vendel', 20)]

# elvárt output: [{'Robi' : 17}, {'Karcsi' : 18}, {'Vendel' : 20}]