dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = {'e': 6, 'f': 4}
dict4 = {'g': 6, 'h': 4}

def my_func(*args):
    import pprint 
    my_temp_dict = {}
    for item in args:
        my_temp_dict.update(item)

    pprint.pprint(my_temp_dict, indent=4)

my_func(dict1, dict2, dict3, dict4)