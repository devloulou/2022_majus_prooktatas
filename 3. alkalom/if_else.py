# vezérlési szerkezetek:

# logikai vizsgálat elvégézése szolgáló eszközkészlet

# docstring
"""
if logikai_vizsgálat:
    utasítások
elif logikai_vizsgálat:
    utasítások
else:
    utasítások

"""



# indentáció, indetálásnak nevezzük
"""
if (a > b) {
    valamit_csinalok;
}
elif (b > a) {
    valamit_csinalok;
}
"""
num1 = 10
num2 = 53

# if num1 > num2: 
#     print(f"num1 nagyobb, értéke: {num1}")
# elif num2 > num1:
#     print(f"num2 nagyobb, értéke: {num2}")
# else:
#     print("egyenlő")


num1 = 10
num2 = 5

# if num1 > num2 and num1/2 == num2:
#     print(num1 + num2)
#     if 2 > 1:
#         print("nagyobb")
#         if 2>3:
#             print("nagyobb2")
#         print("almafa")

# if num1 > num2 and (num1 - num2) > 0:
#     print(num1 - num2)

# null érték

my_null = None
my_null = ()
my_null = []

my_dict = {"kulcs": "érték"}

#print(my_dict.get("alma"))

# not szó a tagadás


"""
num1 = 1
num2 = 1
if num1 == num2:
    csinálj_valamit

if num1 != num2:
    csinálj_valamit

if num1 is num2:
    csinálj_valamait


"""
num1 = 1
num2 = 1

print(id(num1))
print(id(num2))

print(num1 != 1)
print(num1 is num2)

if 'alma' not in ['alma', 'banán']:
    print("benne van az alma")

if my_null is not None:
    print(f"my_null: {my_null}")

if (1,):
    print("a tuple üres")

if None:
    print("a tuple üres")

if []:
    print("a lista üres")

