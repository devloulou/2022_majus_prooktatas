my_list = [1, 2, 3, 4, 5, 6, 7]

print(my_list[2::2])



def my_func(a, b):
    """
    This function powered double the a value then add
    to b, because this need to 
    """
    a *= 2
    return a + b

#clean_code változat
def double_a(a):
    return a*2

def my_func(a, b):
    return double_a(a) + b


if __name__ == '__main__':
    sol = my_func(2, 3)
    print(sol)